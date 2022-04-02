//Arduino Bluetooth Controlled Car
//Before uploading the code you have to install the necessary library
//Note - Disconnect the Bluetooth Module before hiting the upload button otherwise you'll get compilation error message.
//AFMotor Library https://learn.adafruit.com/adafruit-motor-shield/library-install 
//After downloading the library open Arduino IDE >> go to sketch >> Include Libray >> ADD. ZIP Libray >> Select the downloaded 
//ZIP File >> Open it >> Done
//Now You Can Upload the Code without any problem but make sure the bt module isn't connected with Arduino while uploading code

#include <AFMotor.h>

//initial motors pin
AF_DCMotor motor1(1, MOTOR12_1KHZ); 
AF_DCMotor motor2(2, MOTOR12_1KHZ); 
AF_DCMotor motor3(3, MOTOR34_1KHZ);
AF_DCMotor motor4(4, MOTOR34_1KHZ);

char data; 
const int ledPin =  LED_BUILTIN;
int ledState = LOW;

void setup() 
{       
  Serial.begin(9600);  //Set the baud rate to your Bluetooth module.
  pinMode(ledPin, OUTPUT);
  
}

void loop(){
  if(Serial.available() > 0){ 

    data = Serial.read();
    Serial.println(data);

    if (data == '0') {
      digitalWrite(ledPin, LOW);
      Serial.println("OFF");      
    }
    else if (data == '1') {
      digitalWrite(ledPin, HIGH);
      Serial.println("ON");      
    }
  }
}
