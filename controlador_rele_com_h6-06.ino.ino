#include <SoftwareSerial.h>
#define pin1 7 //jumper do rele

SoftwareSerial serial1(10, 11); // RX, TX (coneções do modulo H6-06)

unsigned long delay1 = 0;

void setup() {

  serial1.begin(9600);
  Serial.begin(9600);
  pinMode(pin1,OUTPUT);

}

void loop() {
  char caracter;
  if (serial1.available()) {
    
     caracter = serial1.read();
     Serial.print(caracter);
     
     if(caracter == 'L' ){
        digitalWrite(pin1,LOW);
      }
     if(caracter == 'D' ){
        digitalWrite(pin1,HIGH);
      } 
  }
  
}
