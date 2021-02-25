// Ishaque DHT11
void setup()
{
  Serial.begin(9600);
  
  pinMode(outPin1,OUTPUT);
  pinMode(outPin2,OUTPUT);
  pinMode(outPin3,OUTPUT);
  pinMode(outPin4,OUTPUT);
  
  pinMode(led,OUTPUT);
}
void loop()
{
  if (Serial.available() > 0)
  {
    bt = Serial.read();
    digitalWrite(led, 1);
    
    if(bt == 'F')        //move forwards
    {
      digitalWrite(outPin1,HIGH);
      digitalWrite(outPin2,LOW);
      digitalWrite(outPin3,HIGH);
      digitalWrite(outPin4,LOW);
    }
    else if (bt == 'B')       //move backwards
   #include "DHT.h"
#define DHTPIN 2     
#define DHTTYPE DHT11   

DHT dht(DHTPIN, DHTTYPE);
#include <Wire.h>               
#include <LiquidCrystal_I2C.h>  

LiquidCrystal_I2C lcd(0x27,16,2);
                                  

void setup() {
  lcd.init();  
  lcd.backlight();                

  dht.begin();
}

void loop() {
  
  delay(2000);
  float h = dht.readHumidity();
  float t = dht.readTemperature();
  float f = dht.readTemperature(true);
  float hif = dht.computeHeatIndex(f, h);
  float hic = dht.computeHeatIndex(t, h, false);

  lcd.setCursor(0,0);            
  lcd.print("H: ");
  lcd.print(h);
  lcd.setCursor(0,1);
  lcd.print("T: ");
  lcd.print(t);
  lcd.print(" *C ");
}
