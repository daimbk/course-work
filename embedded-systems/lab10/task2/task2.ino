#include "WiFi.h"
#include <HTTPClient.h>
#include "time.h"

const char* ntpServer = "pool.ntp.org";
const long gmtOffset_sec = 18000; // Adjust for your timezone
const int daylightOffset_sec = 3600;

const char* ssid = "Lounge";
const char* password = "redbrown7";

String GOOGLE_SCRIPT_ID = "AKfycbxR7p9LIBckfXaVeGAYhuNuU02_c4-Aao7_dL8kxvJsL-9bDxd5HwvJrmnKqpQUBVTo";

#define LED_PIN 2
#define BUTTON_PIN 15

bool ledState = false;  // Current state of the LED
bool lastLedState = false; // To track state changes

void setup() {
    Serial.begin(115200);
    delay(1000);
    Serial.println("\nStarting setup...");

    // Configure GPIO pins
    pinMode(LED_PIN, OUTPUT);
    pinMode(BUTTON_PIN, INPUT_PULLUP);

    // Connect to WiFi
    Serial.print("Connecting to WiFi: ");
    Serial.println(ssid);
    WiFi.begin(ssid, password);

    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.print(".");
    }
    Serial.println("\nWiFi connected.");
    configTime(gmtOffset_sec, daylightOffset_sec, ntpServer);
    Serial.println("Time synchronization initialized.");
}

void uploadToGoogleSheet(bool state) {
    if (WiFi.status() == WL_CONNECTED) {
        struct tm timeinfo;
        if (!getLocalTime(&timeinfo)) {
            Serial.println("Failed to obtain time.");
            return;
        }

        // Format date and time separately
        char dateBuff[15], timeBuff[10];
        strftime(dateBuff, sizeof(dateBuff), "%Y-%m-%d", &timeinfo);
        strftime(timeBuff, sizeof(timeBuff), "%H:%M:%S", &timeinfo);

        // Create the URL
        String url = "https://script.google.com/macros/s/" + GOOGLE_SCRIPT_ID + "/exec?ledstatus=" + String(state ? "1" : "0") +
                     "&date=" + String(dateBuff) +
                     "&time=" + String(timeBuff);

        // Send HTTP request
        HTTPClient http;
        http.begin(url);
    }
}

void loop() {
    bool buttonState = !digitalRead(BUTTON_PIN); // Inverted logic for INPUT_PULLUP

    // Toggle LED based on button state
    if (buttonState) {
        if (!ledState) { // Change state only if it’s off
            ledState = true;
            digitalWrite(LED_PIN, HIGH);
            Serial.println("LED turned ON.");
        }
    } else {
        if (ledState) { // Change state only if it’s on
            ledState = false;
            digitalWrite(LED_PIN, LOW);
            Serial.println("LED turned OFF.");
        }
    }

    // Upload only on state change
    if (ledState != lastLedState) {
        uploadToGoogleSheet(ledState);
        lastLedState = ledState;
    }

    delay(500);
}