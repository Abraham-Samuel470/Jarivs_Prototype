#define LED1 7
#define LED2 8
#define LED3 9
#define LED4 10
// Pin connected to the relay module

void setup() {
  pinMode(LED1, OUTPUT);
  digitalWrite(LED1, LOW);
  Serial.begin(9600);
  pinMode(LED2, OUTPUT);
  digitalWrite(LED2, LOW); 
  Serial.begin(9600);
  pinMode(LED3, OUTPUT);
  digitalWrite(LED3, LOW); 
  Serial.begin(9600);
  pinMode(LED4, OUTPUT);
  digitalWrite(LED4, LOW); 
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    String command = Serial.readStringUntil('\n'); // Read the command sent by Python
    command.trim(); // Remove any whitespace

    if (command == "turn on light1") {
      digitalWrite(LED1, HIGH); 
    } else if (command == "turn off light1") {
      digitalWrite(LED1, LOW); }
      
      else if (command == "turn on light2") {
      digitalWrite(LED2, HIGH); }
      else if (command == "turn off light2") {
      digitalWrite(LED2, LOW); }
      
      else if (command == "turn on light3") {
      digitalWrite(LED3, HIGH); }
      else if (command == "turn off light3") {
      digitalWrite(LED3, LOW); }

      else if (command == "turn on light4") {
      digitalWrite(LED4, HIGH); }
      else if (command == "turn off light4") {
      digitalWrite(LED4, LOW); }
    
  }
}
