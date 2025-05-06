#define LED_PIN 2
#define BUTTON_PIN 15

void setup() {
  pinMode(LED_PIN, OUTPUT);
  pinMode(BUTTON_PIN, INPUT_PULLUP);
  Serial.begin(115200);
  Serial.println("Debugging LED and Button...");
}

void loop() {
  bool buttonState = !digitalRead(BUTTON_PIN); // Inverted due to INPUT_PULLUP
  
  if (buttonState) {
    digitalWrite(LED_PIN, HIGH); // Turn LED ON
    Serial.println("Button PRESSED: LED ON");
  } else {
    digitalWrite(LED_PIN, LOW);  // Turn LED OFF
    Serial.println("Button RELEASED: LED OFF");
  }
  delay(200);
}
