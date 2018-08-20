/*by wisemonkey
 * 
*/

const int sensorPin = A0;
const int w = 10; 
const int h = 10; 

void setup() {
  // initialize serial:
  Serial.begin(9600);
  String output = "";
  for(int i = 0; i <= w; i+=1){
    for(int j = 0; j <= h; j+=1){

     int val = analogRead(sensorPin); 
     output += String(val);
     output += ","; 
     delay(10);   
    }
    output+="\n";
  }

  output += "end";
  Serial.print(output);

}

void loop() {
  
}
