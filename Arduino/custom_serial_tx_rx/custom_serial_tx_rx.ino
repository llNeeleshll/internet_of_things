#include<SoftwareSerial.h>

char data; 
const int ledPin =  LED_BUILTIN;
int ledState = LOW;

SoftwareSerial mySerial(2,3); // Rx, Tx


void setup() 
{       
  Serial.begin(9600);
  mySerial.begin(9600);  //Set the baud rate to your Bluetooth module.
  pinMode(ledPin, OUTPUT);
  
}

void loop(){
  if(mySerial.available() > 0){ 

    data = mySerial.read();
    Serial.println(data);

    if (data == '0') {
      digitalWrite(ledPin, LOW);
      mySerial.println("OFF");      
    }
    else if (data == '1') {
      digitalWrite(ledPin, HIGH);
      mySerial.println("ON");      
    }
  }
}
