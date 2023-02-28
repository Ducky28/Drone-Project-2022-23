
#define PWMController1Pin 3;
#define  PWMController2Pin 5;

#define STOP 0
#define SPIN_MOTORS 1
#define FIRE 2
#define RELOAD 3

#define SHOOTER_DELAY 1000

int shooterStage = 0; 

void setup(){
  Serial.begin(115200);

  pinMode(PWMController1Pin, OUTPUT);
  pinMode(PWMController2Pin, OUTPUT);

  Serial.println("FINISHED INIT, BEGINNING LOOP");
}

void loop(){
  switch(shooterStage){

    case STOP:
      analogWrite(PWMController1Pin, LOW);
      analogWrite(PWMController2Pin, LOW);
      break;

    case SPIN_MOTORS:
      analogWrite(PWMController1Pin, HIGH);
      analogWrite(PWMController2Pin, HIGH);
      break;

    case FIRE:
      delayMicroseconds(SHOOTER_DELAY);
      break;

    case RELOAD:

      analogWrite(PWMController1Pin, LOW);
      analogWrite(PWMController2Pin, LOW);
      break;

  }
  
}
