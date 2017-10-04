// version 0.0.1

const int speedM = 11; // initialize enable pins in motor driver

const int m1 = 2; // initialize motor pins
const int m2 = 3;

const int echo = 10; // initialize echo pin for U.S. sensor
const int trig = 9; // initialize trigger pin for U.S. sensor

const int piStop = 7; // stop sign detection from pi
const int piLight = 6; // street light detection from pi

int spd=200; // speed of the motors

double timeDelay = 0; // initialize time delay between triger and echo
double distance = 0; // initialize distance of obstacle

boolean obstacle = false;



void setup()
{
  Serial.begin(9600);
  
  pinMode(speedM,OUTPUT);

  pinMode(m1,OUTPUT);
  pinMode(m2,OUTPUT);

  pinMode(trig,OUTPUT);
  pinMode(echo,INPUT);

  pinMode(piStop, INPUT);
  pinMode(piLight, INPUT);
}

void loop-with-ultrasonic()
{
  analogWrite(speedM,spd); // speed of left motor
  if(!spd)
    stopNow();
  else
    forward();

  pulseOut(); // triggers the pulse

  timeDelay = pulseIn(echo,HIGH); // recieves the echo
  distance = timeDelay * 0.017; // in cm

  Serial.print(spd);
  Serial.print(" : ");
  Serial.println(distance);

  if( distance < 10 )  // U.S obstacle
  {
    spd = 0;
  }
  else if(digitalRead(piLight))  // Street light red/green
  {
    spd = 0;
  }
  else if(digitalRead(piStop)) // stop sign detection
  {
    spd = 0;
    analogWrite(speedM,spd);
    delay(10000);
    spd = 200;
  }
  else
    spd =200;
}

void loop()
{
  analogWrite(speedM,spd); // speed of left motor
  if(!spd)
    stopNow();
  forward();

  Serial.println(spd);
  
  if(digitalRead(piLight))  // Street light red/green
  {
    spd = 0;
  }
  else if(digitalRead(piStop)) // stop sign detection
  {
    spd = 0;
    analogWrite(speedM,spd);
    delay(10000);
    spd = 200;
  }
  else
    spd =200;
}

void pulseOut()
{
  digitalWrite(trig,0);
  delayMicroseconds(2);
  
  digitalWrite(trig,1);
  delayMicroseconds(10); // trigger HIGH pulse
  
  digitalWrite(trig,0);// return back to LOW
}

void forward()
{
  digitalWrite(m1,1);
  digitalWrite(m2,0);// wheels forward
}

void backward()
{
  digitalWrite(m1,0);
  digitalWrite(m2,1);// wheels backward
}

void stopNow()
{
  digitalWrite(m1,0);
  digitalWrite(m2,0);// wheels stop
  delay(1000);
}

