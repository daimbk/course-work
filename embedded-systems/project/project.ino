#include <WiFi.h>
#include <WebServer.h>
#include <HTTPClient.h>
#include "time.h"

// Wi-Fi Credentials
const char* ssid = "Ufone_1D36D8";
const char* password = "Lahore@890";

// Google Apps Script Web App URL
String GOOGLE_SCRIPT_URL = "https://script.google.com/macros/s/AKfycbwFUVueorravojiCVTKlM_BbtSpf1flURO1AUkxe-8-BE3G3Ipl8pZP8p0-GiX10po/exec";

// GPIO Pins for LEDs
#define LED1 2
#define LED2 4
#define LED3 18
#define LED4 19

// GPIO Pins for Buttons
#define BUTTON1 26
#define BUTTON2 25
#define BUTTON3 33
#define BUTTON4 32

// NTP Time Configuration
const char* ntpServer = "pool.ntp.org";
const long gmtOffset_sec = 3600 * 5; // Adjust for your timezone (e.g., GMT+5)
const int daylightOffset_sec = 0;

// Variables to Track LED States
bool ledState1 = false;
bool ledState2 = false;
bool ledState3 = false;
bool ledState4 = false;

// Variables to Track Previous States for Debounce
bool lastButtonState1 = HIGH;
bool lastButtonState2 = HIGH;
bool lastButtonState3 = HIGH;
bool lastButtonState4 = HIGH;

// Debounce Timing
unsigned long lastDebounceTime1 = 0;
unsigned long lastDebounceTime2 = 0;
unsigned long lastDebounceTime3 = 0;
unsigned long lastDebounceTime4 = 0;
unsigned long debounceDelay = 50;

// Web server on port 80
WebServer server(80);

// HTML content
const char htmlPage[] PROGMEM = R"rawliteral(
<!DOCTYPE html>
<html>
<head>
  <title>LED ON Duration</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <style>
    body { font-family: Arial, sans-serif; text-align: center; margin: 0; padding: 0; background-color: #121212; color: #ffffff; }
    h1 { margin-top: 20px; color: #f2f2f2; }
    form { display: flex; flex-direction: column; align-items: center; margin: 20px auto; padding: 20px; border-radius: 10px; background-color: #1e1e1e; box-shadow: 0 0 10px rgba(0, 0, 0, 0.5); max-width: 90%; }
    label { margin-top: 10px; font-size: 18px; }
    input, button { padding: 10px; margin: 10px; font-size: 16px; border: none; border-radius: 5px; width: 90%; max-width: 400px; }
    input { background-color: #2e2e2e; color: #ffffff; }
    button { background-color: #03a9f4; color: #ffffff; cursor: pointer; }
    button:hover { background-color: #0288d1; }
    #result { margin-top: 20px; font-weight: bold; font-size: 18px; }
    @media (max-width: 768px) { h1 { font-size: 24px; } label { font-size: 16px; } input, button { font-size: 14px; } }
  </style>
</head>
<body>
  <h1>LED ON Duration Tracker</h1>
  <form id="ledForm">
    <label for="led">LED ID:</label>
    <input type="number" id="led" name="led" required>
    <label for="startDateTime">Start Date & Time:</label>
    <input type="datetime-local" id="startDateTime" name="startDateTime" required>
    <label for="endDateTime">End Date & Time:</label>
    <input type="datetime-local" id="endDateTime" name="endDateTime" required>
    <button type="button" onclick="getOnDuration()">Get ON Duration</button>
  </form>
  <div id="result"></div>
  <script>
    async function getOnDuration() {
      const led = document.getElementById("led").value;
      const startDateTime = document.getElementById("startDateTime").value.replace("T", " ");
      const endDateTime = document.getElementById("endDateTime").value.replace("T", " ");

      if (!led || !startDateTime || !endDateTime) {
        alert("Please fill all fields.");
        return;
      }

      const url = `/getOnTime?led=${led}&startDateTime=${startDateTime}&endDateTime=${endDateTime}`;
      try {
        const response = await fetch(url);
        const data = await response.json();
        document.getElementById("result").innerHTML =
          `Total ON Time: ${data.hours} hours, ${data.minutes} minutes, ${data.seconds} seconds`;
      } catch (error) {
        console.error("Error:", error);
        document.getElementById("result").innerHTML = "Error: Unable to fetch data.";
      }
    }
  </script>
</body>
</html>
)rawliteral";

// Function to get ON time from Google Apps Script
void handleGetOnTime() {
  if (!server.hasArg("led") || !server.hasArg("startDateTime") || !server.hasArg("endDateTime")) {
    server.send(400, "application/json", "{\"error\":\"Missing parameters\"}");
    return;
  }

  String led = server.arg("led");
  String startDateTime = server.arg("startDateTime");
  String endDateTime = server.arg("endDateTime");

  String url = GOOGLE_SCRIPT_URL + "?led=" + led + "&startDateTime=" + startDateTime + "&endDateTime=" + endDateTime;

  HTTPClient http;
  http.begin(url);
  http.setFollowRedirects(HTTPC_FORCE_FOLLOW_REDIRECTS); // Handle redirections automatically

  int httpCode = http.GET();
  if (httpCode > 0) {
    String response = http.getString();
    server.send(200, "application/json", response);
  } else {
    server.send(500, "application/json", "{\"error\":\"Failed to fetch data\"}");
  }

  http.end();
}

// Function to upload LED state to Google Sheets
void uploadToGoogleSheet(int led, bool state) {
  if (WiFi.status() == WL_CONNECTED) {
    struct tm timeinfo;
    if (!getLocalTime(&timeinfo)) {
      Serial.println("Failed to obtain time");
      return;
    }

    // Properly format DateTime as "YYYY-MM-DD-HH:MM:SS"
    char dateTimeBuffer[20];
    strftime(dateTimeBuffer, sizeof(dateTimeBuffer), "%Y-%m-%d %H:%M:%S", &timeinfo);

    char formatDateTime[40];
    int i = 0;
    for (int j = 0; j < strlen(dateTimeBuffer); j++) {
      if (dateTimeBuffer[j] == ' ') {
        formatDateTime[i++] = '%';
        formatDateTime[i++] = '2';
        formatDateTime[i++] = '0';
      } else {
        formatDateTime[i++] = dateTimeBuffer[j];
      }
    }
    formatDateTime[i] = '\0';

    // Construct the URL with all parameters
    String url = GOOGLE_SCRIPT_URL
                 + "?led=" + String(led)
                 + "&status=" + String(state ? "ON" : "OFF")
                 + "&dateTime=" + formatDateTime;

    Serial.println("Request URL: " + url); // Debug log for the URL

    HTTPClient http;
    http.begin(url); // Initialize HTTPClient with the URL
    int httpCode = http.GET(); // Send GET request

    if (httpCode > 0) {
      String response = http.getString();
      Serial.println("Response: " + response); // Log response from Google Apps Script
    } else {
      Serial.printf("HTTP request failed with error: %s\n", http.errorToString(httpCode).c_str());
    }

    http.end();
  } else {
    Serial.println("WiFi Disconnected!");
  }
}

void setup() {
  Serial.begin(115200);

  // Setup LEDs as Outputs
  pinMode(LED1, OUTPUT);
  pinMode(LED2, OUTPUT);
  pinMode(LED3, OUTPUT);
  pinMode(LED4, OUTPUT);

  // Setup Buttons as Inputs with Pullup Resistors
  pinMode(BUTTON1, INPUT_PULLUP);
  pinMode(BUTTON2, INPUT_PULLUP);
  pinMode(BUTTON3, INPUT_PULLUP);
  pinMode(BUTTON4, INPUT_PULLUP);

  // Connect to Wi-Fi
  Serial.println("Connecting to WiFi...");
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nWiFi Connected");

  // Configure NTP Time
  configTime(gmtOffset_sec, daylightOffset_sec, ntpServer);

  // Serve HTML page
  server.on("/", []() {
    server.send(200, "text/html", htmlPage);
  });

  // Register the /getOnTime endpoint
  server.on("/getOnTime", handleGetOnTime);

  // Start the server
  server.begin();
  Serial.println("HTTP server started");
  Serial.println(WiFi.localIP());
}

void loop() {
  // Read Button States
  bool buttonState1 = digitalRead(BUTTON1);
  bool buttonState2 = digitalRead(BUTTON2);
  bool buttonState3 = digitalRead(BUTTON3);
  bool buttonState4 = digitalRead(BUTTON4);

  unsigned long currentTime = millis();

  // Handle Button 1
  if (buttonState1 != lastButtonState1 && (currentTime - lastDebounceTime1 > debounceDelay)) {
    lastDebounceTime1 = currentTime;
    if (buttonState1 == LOW) { // Button Pressed
      ledState1 = !ledState1; // Toggle LED State
      digitalWrite(LED1, ledState1 ? HIGH : LOW);
      uploadToGoogleSheet(1, ledState1);
    }
  }
  lastButtonState1 = buttonState1;

  // Handle Button 2
  if (buttonState2 != lastButtonState2 && (currentTime - lastDebounceTime2 > debounceDelay)) {
    lastDebounceTime2 = currentTime;
    if (buttonState2 == LOW) {
      ledState2 = !ledState2;
      digitalWrite(LED2, ledState2 ? HIGH : LOW);
      uploadToGoogleSheet(2, ledState2);
    }
  }
  lastButtonState2 = buttonState2;

  // Handle Button 3
  if (buttonState3 != lastButtonState3 && (currentTime - lastDebounceTime3 > debounceDelay)) {
    lastDebounceTime3 = currentTime;
    if (buttonState3 == LOW) {
      ledState3 = !ledState3;
      digitalWrite(LED3, ledState3 ? HIGH : LOW);
      uploadToGoogleSheet(3, ledState3);
    }
  }
  lastButtonState3 = buttonState3;

  // Handle Button 4
  if (buttonState4 != lastButtonState4 && (currentTime - lastDebounceTime4 > debounceDelay)) {
    lastDebounceTime4 = currentTime;
    if (buttonState4 == LOW) {
      ledState4 = !ledState4;
      digitalWrite(LED4, ledState4 ? HIGH : LOW);
      uploadToGoogleSheet(4, ledState4);
    }
  }
  lastButtonState4 = buttonState4;

  // Handle Web Server Requests
  server.handleClient();
}
