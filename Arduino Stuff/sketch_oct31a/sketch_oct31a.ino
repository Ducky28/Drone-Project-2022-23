#include <Servo.h>

Servo servo; 

const int servoPin; // will act as a substitute for the plunger for now
const int motorPin1;
const int motorPin2;

int servoPos;
String state;

void setup() {
  // put your setup code here, to run once:

  Serial.begin(19200);
  servo.attach(servoPin);
  servo.write(0);

  pinMode(servoPin, OUTPUT);
  pinMode(motorPin1, OUTPUT);
  pinMode(motorPin2, OUTPUT);

}

void loop() {

    while(Serial.available()==0){
      Serial.print("CANT REACH SERIAL PORT");
    }
    
    state = Serial.readLines();

    switch(state){
      case "STOP":

        servo.write(0);
        digitalWrite(motorPin1, LOW);
        digitalWrite(motorPin2, LOW);

        break;

      case "SPIN MOTORS":

        digitalWrite(motorPin1, HIGH);
        digitalWrite(motorPin2, HIGH);

        break;

        case "FIRE":

          servo.write(180);
          break
    }
    
}