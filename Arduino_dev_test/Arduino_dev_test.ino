/*by wisemonkey
 * 
*/

const int sensorPin = A0;
const int w = 100; 
void setup() {
  // initialize serial:
  Serial.begin(9600);
  // reserve 200 bytes for the inputString:
//  if (Serial.available()>0) {
    for(int i = 0; i <= w; i+=1){
       int val = analogRead(sensorPin); 
       Serial.print(val);
       Serial.print(","); 
       delay(50);   
    }
    Serial.print("end");
//  }
}

void loop() {
  
}
