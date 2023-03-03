#include <Servo.h>

#define SERVO_PIN 1;

Servo servo;

void setup(){
    servo.attach(SERVO_PIN);
    servo.write(0);
}

void loop(){

    for(int i = 0; i < 180;i++){
        servo.write(i);
    }

    for(int j = 0; j > 0; j++){
        servo.write(j);
    }

}
