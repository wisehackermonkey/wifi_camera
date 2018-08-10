#include <Stepper.h>

const int stepsPerRevolution = 2158;  
Stepper baseMotor(stepsPerRevolution, 8, 10, 9, 11);
Stepper antMotor(stepsPerRevolution, 4, 5, 6, 7);

int stepCount = 0;  
int target = 20;
String inString = "";    // string to hold input


void setup() {
  Serial.begin(9600);
   while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }
   // send an intro:
  Serial.println("\n\nStepper Controller: ");
  Serial.println();
}

void loop() {
  while (Serial.available() > 0) {
    //https://www.arduino.cc/en/Tutorial/StringToInt
      int inChar = Serial.read();
      if (isDigit(inChar) || inChar == ',') {
        inString += (char)inChar;
      }
      //when full "84,22" string is read by serial 
      //start to parse into 84 and 22 as int's
      if(inChar == '\n'){
        //https://stackoverflow.com/questions/11068450/arduino-c-language-parsing-string-with-delimiter-input-through-serial-interfa#14306981
        Serial.println(inString);
        int delimiterPosition  = inString.indexOf(',');
        
        if(delimiterPosition >= 0){
          
          String servoPos1 = inString.substring(0, delimiterPosition);//[123],456
          String servoPos2 = inString.substring(delimiterPosition + 1,inString.length());//123,[456]
          
          int pos1 = servoPos1.toInt();
          int pos2 = servoPos2.toInt();
          
          Serial.print("Pos1: ");
          Serial.println(pos1);
          Serial.print(", Pos2: ");
          Serial.println(pos2);
          
          Serial.println("Steps:");
          for(int i = 0; i <= pos1; i +=1){
            baseMotor.step(1);
            Serial.print(".");
              delay(20);
          }
          for(int i = 0; i <= pos2; i +=1){
            antMotor.step(1);
            Serial.print(".");
              delay(20);
          }
        }
      // clear the string for new input:
      inString = "";
      }
      
      
  }



  
//  Serial.println("Steps:");
//  for(int i = 0; i < target; i +=1){
//    baseMotor.step(1);
//    Serial.print(".");
//      delay(20);
//  }
//  delay(1000);
//  Serial.println();
}

