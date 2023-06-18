// Define Motor Pin Number
#define A1 5  // Yello (A-1B)
#define A2 6  // Green (A-1A)

int incomingByte = 0; // serial data

void setup() {

  pinMode(A1, OUTPUT);
  pinMode(A2, OUTPUT);

  digitalWrite(A1, LOW);
  digitalWrite(A2, LOW);
  
  Serial.begin(9600);

  Serial.println("select mode");
  Serial.println("1.long movement");
  Serial.println("2.short movement");
  Serial.println("3.stop");

}
int  input = 0;
void loop() {

  // send data only when you receive data:
  if (Serial.available() > 0) {
    // read the incoming byte:
    incomingByte = Serial.read();
    input = incomingByte - 48; //convert ASCII code

  switch (input) { 
    case 1:         // if input=1 ....... motor turn counter-clockwise for long period
      forward_long();
      break;
    case 2:         // if input=2 ....... motor turn counter-clockwise for short period
      forward_short();
      break;
    case 3:         // if input=1 ....... motor stop
      Stop();
      break;
  }
  delay(200);
  input=0;
}
}
void forward_long() {          //counter-clockwise for long period
  for(int i=0; i<12; i++)
  {
    analogWrite(A1, 255);
    analogWrite(A2, 0);
    delay(50);
    digitalWrite(A1, LOW);
    digitalWrite(A2, LOW);
    delay(50);
  }
}

void forward_short() {          //counter-clockwise for short period
  for(int i=0; i<1; i++)
  {
    analogWrite(A1, 255);
    analogWrite(A2, 0);
    delay(50);
    digitalWrite(A1, LOW);
    digitalWrite(A2, LOW);
    delay(70);
  }
}

void Stop() {              //function of stop
  digitalWrite(A1, LOW);
  digitalWrite(A2, LOW);
}
