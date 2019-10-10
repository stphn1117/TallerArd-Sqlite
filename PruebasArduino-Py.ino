const int pinLED = 13;
 
void setup() 
{ //se establace  la conexión al serial
  // iniciando con 9600 (velocidad de lectura de datos)
   Serial.begin(9600);
   pinMode(pinLED, OUTPUT);
}
 
void loop(){
  int lectura = analogRead(0);
  Serial.println(lectura);
  delay(1000);
  /*
int lectura = analogRead(0);
Serial.println(lectura);
delay(1000);

//lecturas cada segundo
   if (Serial.available()>0){
   

   observar la cantidad de datos que entran al buffer
   e irlos sacando uno a uno hasta que se cumpla la condicional
   todo lo que llega se guarda en rx y luego se envía con el serial

   
    char rx = Serial.read();
    Serial.print(rx);
    if (Serial.read() == 107){
      // Se envia el caracter 445.45
      Serial.println(445.45);
      }
    /*
      char option = Serial.read();
      if (option >= '1' && option <= '9')
      {
         option -= '0';
         for (int i = 0;i<option;i++) 
         {
            digitalWrite(pinLED, HIGH);
            delay(100);
            digitalWrite(pinLED, LOW);
            delay(200);
         }
      }
      */
   
}
