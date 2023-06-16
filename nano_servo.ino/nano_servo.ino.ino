#include <Servo.h>

Servo myservo;  // create servo object to control a servo
int pos = 0;    // variable to store the servo position

void setup() {
  Serial.begin(9600);  // initialize serial communication at 9600 bits per second
  myservo.attach(9);  // attaches the servo on pin 9 to the servo object
}

void loop() {
  if (Serial.available()){
    // check if data is available on the serial port
    char command = Serial.read();
    
    if (command == '180'){
      // if the command is 'A'
      pos = 180; // set the position to 180 degrees
    }
    else if (command == '-180'){
      // if the command is 'B'
      pos = -180;  // set the position to -180 degrees
    }
    else{
      // if the command is anything else
      pos = 0;  // set the position to 0 degrees (default)
    }
    myservo.write(pos);// move the servo to the desired position
    Serial.print("Motor position: ");// print the motor position
    Serial.println(pos);
  }
}
