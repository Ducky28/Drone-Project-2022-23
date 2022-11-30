#include <Servo.h>
#include <ezButton.h>
#include <HardwareSerial.h>

Servo servo;
String coords;
String subString;
int servoPos;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(19200);
  servo.attach(7);
  pinMode(7,OUTPUT);
  servo.write(0);
}

void loop() {
    while(Serial.available()==0){
      Serial.print("CANT REACH SERIAL PORT");
    }
    
    coords = Serial.readString();
    subString = coords.substring(0,2);
    servoPos = int(subString.toInt());
    servo.write(servoPos);
    z
}