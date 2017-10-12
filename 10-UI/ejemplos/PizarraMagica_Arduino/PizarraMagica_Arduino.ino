void setup () {
  Serial.begin(9600);
}
 
void loop () {
  int potx = getAverage(A0, 500);
  int poty = getAverage(A1, 400);	
  sendData(potx, poty);
}

void sendData(int x, int y) {  
   Serial.print(x);
   Serial.print(",");
   Serial.print(y);
   Serial.println("");  
}

int getAverage(int x, int y) {
  int value = 0;
  for(int i=0; i< 5; i++) {
    value =   value + map(analogRead(x), 0, 1023, 0, y);
  }
  
  value = value / 5;
  return value;
}
