int sensorState = 0;

void setup()
{
  pinMode(2, INPUT);
  pinMode(12, OUTPUT);
  Serial.begin(9600);
}

void loop()
{
  // read the state of the sensor/digital input
  sensorState = digitalRead(2);
  // check if sensor pin is HIGH. if it is, set the
  // LED on.
  if (sensorState == HIGH) {
    digitalWrite(12, 1);
    Serial.println("Sensor activated!");
    delay(2000);
  } else {
    digitalWrite(12, 0);
    Serial.println("Sensor deactivated!");
    
  }
  // Delay a little bit to improve simulation performance
}
