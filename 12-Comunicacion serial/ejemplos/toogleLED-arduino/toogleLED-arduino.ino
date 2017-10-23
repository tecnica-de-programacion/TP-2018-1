int led = 13;

void setup() {
   Serial.begin(115200);
   pinMode(led, OUTPUT);
   digitalWrite(led, LOW);
}

void loop() { }

void serialEvent() {
    char inChar = (char)Serial.read();
    int state = inChar == '1' ? HIGH : LOW;
    digitalWrite(led, state);
}
