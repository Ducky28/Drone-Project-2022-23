#include <Servo.h>

Servo servo; 
Servo fakeMotor;

const int servoPin = 7; // will act as a substitute for the plunger for now
const int motorPin1 = 8;
//const int motorPin2;

String state;

int servoPos;

void setup() {
  // put your setup code here, to run once:

  Serial.begin(9600);
  servo.attach(servoPin);
  servo.write(0);

  fakeMotor.attach(motorPin1);
  fakeMotor.write(0);

  //pinMode(servoPin, OUTPUT);
  //pinMode(motorPin1, OUTPUT);
  //pinMode(motorPin2, OUTPUT);

}

void loop() {

    while(Serial.available()==0){
      Serial.print("CANT REACH SERIAL PORT");
    }

    // Will definitely need to be updated once esc arrives in the mail
    if(Serial.available() > 0){
      state = Serial.readString();
      
      if(state == "STOP"){

        servo.write(0);
        fakeMotor.write(0);

      }else if(state == "SPIN_MOTORS"){

        fakeMotor.write(180);

      }else if(state == "FIRE"){

        servo.write(180);

      }else if(state == "RELOAD"){

        fakeMotor.write(0);
        servo.write(0);

      }else{

        Serial.print("BRO WTF IS GOING ON???");

      }
    }
}