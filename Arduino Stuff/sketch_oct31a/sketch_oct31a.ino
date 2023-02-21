#define motor1Pin 1
#define motor2Pin 7

void setup(){
    pinMode(motor1Pin, OUTPUT);
    pinMode(motor2Pin, OUTPUT);
}

void loop(){
    analogWrite(motor1Pin, HIGH);
    analogWrite(motor2Pin, HIGH);
}
