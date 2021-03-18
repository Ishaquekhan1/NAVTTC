import sys
import urllib2
from time import sleep
import Adafruit_DHT as dht
import pathlib
from datetime import datetime
def DHT11_data():
import time,board, adafruit_dht
    dhtDevice= adafruit_dht.DHT11(board.D23)
    myAPI='UVU6C4MT914RDT81'
    baseURL='https://api.thingspeak.com/update?api_key=%s' % myAPI
while True:
   try:
       Time=str(time.strftime("%I:%M:%S:%p", time.localtime()))
       currentdate= str(datetime.now().day) + ',' + str(datetime.now().month) + ',' + str(datetime.now().year)
       temperature_c = dhtDevice.temperature
       temperature_f = temperature_c * (9 / 5) + 32
       humidity = dhtDevice.humidity
       conn=urllib2.urlopen(baseURL + '&field1=%s&field2=%s'%(temp, humi))
        print conn.read()
        conn.close()
        print("Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(temperature_f, temperature_c, humidity))
   except RuntimeError as error:
       # Errors happen fairly often, DHT's are hard to read, just keep going
       print(error.args[0])
       time.sleep(2.0)
       continue
   except Exception as error:
       dhtDevice.exit()
       raise error
       time.sleep(2.0)
       path="/home/pi/iot-batch2/value.csv"
       p=pathlib.Path(path)
   if p.exists():
       with open(path,"a+") as file:
           file.write(str(temperature_c)+','+str(temperature_f)+','+str(humidity)+','+str(currentdate)+','+str(Time))
           file.write("\n")
   else:
       with open(path,"a+") as file:
           file.write(str("Celcius Temperature")+','+str("Fahrenheit Temperature")+','+str("Humidity")+','+str("Date")+','+str("Month")+','+str("Year")+','+str("Time"))
           file.write("\n")
           file.write(str(temperature_c)+','+str(temperature_f)+','+str(humidity)+','+str(currentdate)+','+str(Time))
           file.write("\n")