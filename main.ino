#include <SoftwareSerial.h>
#define rele_1 8 //INI1 do rele 1
#define rele_2 9 //INI2 do rele 2
SoftwareSerial bluetooth(10, 11); // 10 pino do TX do HC-06, 11 pino RX do HC-06

void setup() {

  bluetooth.begin(9600);
  Serial.begin(9600);

  pinMode(rele_1,OUTPUT);
  pinMode(rele_2,OUTPUT);

  digitalWrite(rele_1,HIGH);
  digitalWrite(rele_2,HIGH);
}

String leStringSerial(){
  String conteudo = "";
  char caractere;
  
  // Enquanto receber algo pela serial
  while(bluetooth.available()) {
    // Lê byte da serial
    caractere = bluetooth.read();
    // Ignora caractere de quebra de linha
    if (caractere != '\n'){
      // Concatena valores
      conteudo.concat(caractere);
    }
    // Aguarda buffer serial ler próximo caractere
    delay(10);
  }
    
  Serial.print("Recebi: ");
  Serial.println(conteudo);
    
  return conteudo;
}

void loop() {
  String dado_recebido;
  
  if (bluetooth.available()) {
    
     dado_recebido = leStringSerial();
     
     if(dado_recebido == "Rele01:on" ){
        digitalWrite(rele_1,HIGH); 
     }
     if(dado_recebido == "Rele01:off" ){
        digitalWrite(rele_1,LOW);
     }

     if(dado_recebido == "Rele02:on" ){
        digitalWrite(rele_2,HIGH); 
     }
     if(dado_recebido == "Rele02:off" ){
        digitalWrite(rele_2,LOW);
     } 
  }
}