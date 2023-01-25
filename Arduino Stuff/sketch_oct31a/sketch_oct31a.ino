#include <Servo.h>

Servo servo;

int servoPin = 9;

int PWMController1Pin = 3;
int PWMController2Pin = 5;

int servoStartPos = 0;
int servoReadyPos = 180; 
int servoFirePos = 0;

#define SPIN_MOTORS 0
#define PREP_SERVO 1
#define FIRE 2
#define RELOAD 3

int shooterStage = 0; 

void setup(){
  pinMode(PWMController1Pin, OUTPUT);
  pinMode(PWMController2Pin, OUTPUT);
  servo.attach(servoPin);
}

void loop(){
  switch(shooterStage){

    case SPIN_MOTORS:
      analogWrite(PWMController1Pin, HIGH);
      analogWrite(PWMController2Pin, HIGH);
      break;

    case PREP_SERVO:
      servo.write(servoReadyPos);
      break

    case FIRE:
      servo.write(servoFirePos);
      break;

    case RELOAD:
      servo.write(servoStartPos);
      analogWrite(PWMController1Pin);
      analogWrite(PWMController2Pin);

  }
  
}