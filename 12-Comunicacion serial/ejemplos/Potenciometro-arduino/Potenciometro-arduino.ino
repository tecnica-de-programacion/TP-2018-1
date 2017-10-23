int sensorPin = A0;
int potValue = 0;
int mapValue = 0;

void setup() {
   Serial.begin(115200);
}

void loop() {
  int sensorValue = analogRead(sensorPin); 
  sendData(sensorValue);
}

void sendData(int value) {
  mapValue = map(value, 0, 1023, 0, 400);
  Serial.print(value);
  Serial.print(",");
  Serial.println(mapValue);
}
