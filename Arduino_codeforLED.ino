#define RELAY_PIN 7  // Pin connected to the relay module

void setup() {
  pinMode(RELAY_PIN, OUTPUT);
  digitalWrite(RELAY_PIN, LOW); // Start with the relay off
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    String command = Serial.readStringUntil('\n'); // Read the command sent by Python
    command.trim(); // Remove any whitespace

    if (command == "turn on light") {
      digitalWrite(RELAY_PIN, HIGH); // Turn on the relay
    } else if (command == "turn off light") {
      digitalWrite(RELAY_PIN, LOW); // Turn off the relay
    }
  }
}
