#include <AFMotor.h>
#include "SoftwareSerial.h"
#include "DFRobotDFPlayerMini.h"

static const int PIN_MP3_TX = 5; // Connects to module's RX 
static const int PIN_MP3_RX = 4; // Connects to module's TX 

SoftwareSerial player_serial(PIN_MP3_RX, PIN_MP3_TX);

AF_DCMotor motor1(1, MOTOR12_1KHZ); 
AF_DCMotor motor2(2, MOTOR12_1KHZ); 
AF_DCMotor motor3(3, MOTOR34_1KHZ);
AF_DCMotor motor4(4, MOTOR34_1KHZ);

DFRobotDFPlayerMini player;

int trigger_pin = 2;
int echo_pin = 3;

char movement, command; 

int motor_speed = 140;
int stop_distance = 30;

void setup() 
{       
  Serial.begin(9600);  //Set the baud rate to your Bluetooth module.
  player_serial.begin(9600);

  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, LOW);

  player.setTimeOut ( 1000 ) ;

  if (player.begin(player_serial)) {

    digitalWrite(LED_BUILTIN, HIGH);
    
    player.volume(30);
    delay(20);
    player.play(2);
  
  }
  
  pinMode(trigger_pin, OUTPUT);
  pinMode(echo_pin, INPUT);
  Stop();
}

void loop(){

  long distance_of_obstacle = initialize_and_get_distance_sensor();
   
  if(Serial.available() > 0){ 
    
    command = Serial.read();
    movement = command;
    
    Stop(); //initialize with motors stoped
    
    Serial.println(command);
    
    switch(command){
    case 'F':  
      forward();
      break;
    case 'B':  
       back();
      break;
    case 'L':  
      left();
      break;
    case 'R':
      right();
      break;    
    case 'S':
      Stop();
      break;
    }
    
  } 

  if(distance_of_obstacle < stop_distance && movement == 'F'){
    Stop();
  }
  
}

long initialize_and_get_distance_sensor(){

   long duration, distance_of_obstacle;

   digitalWrite(trigger_pin, HIGH);
   delayMicroseconds(1000);
   digitalWrite(trigger_pin, LOW);

   duration = pulseIn(echo_pin, HIGH);
   distance_of_obstacle = (duration/2)/29.1;

   return distance_of_obstacle;
  
}

void forward()
{
  motor1.setSpeed(motor_speed); //Define maximum velocity
  motor1.run(FORWARD); //rotate the motor clockwise
  motor2.setSpeed(motor_speed); //Define maximum velocity
  motor2.run(FORWARD); //rotate the motor clockwise
  motor3.setSpeed(motor_speed);//Define maximum velocity
  motor3.run(FORWARD); //rotate the motor clockwise
  motor4.setSpeed(motor_speed);//Define maximum velocity
  motor4.run(FORWARD); //rotate the motor clockwise
}

void back()
{
  motor1.setSpeed(motor_speed); //Define maximum velocity
  motor1.run(BACKWARD); //rotate the motor anti-clockwise
  motor2.setSpeed(motor_speed); //Define maximum velocity
  motor2.run(BACKWARD); //rotate the motor anti-clockwise
  motor3.setSpeed(motor_speed); //Define maximum velocity
  motor3.run(BACKWARD); //rotate the motor anti-clockwise
  motor4.setSpeed(motor_speed); //Define maximum velocity
  motor4.run(BACKWARD); //rotate the motor anti-clockwise
}

void left()
{
  motor1.setSpeed(motor_speed); //Define maximum velocity
  motor1.run(BACKWARD); //rotate the motor anti-clockwise
  motor2.setSpeed(motor_speed); //Define maximum velocity
  motor2.run(BACKWARD); //rotate the motor anti-clockwise
  motor3.setSpeed(motor_speed); //Define maximum velocity
  motor3.run(FORWARD);  //rotate the motor clockwise
  motor4.setSpeed(motor_speed); //Define maximum velocity
  motor4.run(FORWARD);  //rotate the motor clockwise
}

void right()
{
  motor1.setSpeed(motor_speed); //Define maximum velocity
  motor1.run(FORWARD); //rotate the motor clockwise
  motor2.setSpeed(motor_speed); //Define maximum velocity
  motor2.run(FORWARD); //rotate the motor clockwise
  motor3.setSpeed(motor_speed); //Define maximum velocity
  motor3.run(BACKWARD); //rotate the motor anti-clockwise
  motor4.setSpeed(motor_speed); //Define maximum velocity
  motor4.run(BACKWARD); //rotate the motor anti-clockwise
} 

void Stop()
{
  motor1.setSpeed(0); //Define minimum velocity
  motor1.run(RELEASE); //stop the motor when release the button
  motor2.setSpeed(0); //Define minimum velocity
  motor2.run(RELEASE); //rotate the motor clockwise
  motor3.setSpeed(0); //Define minimum velocity
  motor3.run(RELEASE); //stop the motor when release the button
  motor4.setSpeed(0); //Define minimum velocity
  motor4.run(RELEASE); //stop the motor when release the button
}
