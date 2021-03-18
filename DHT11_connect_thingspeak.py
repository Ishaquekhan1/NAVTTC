import sys
import urllib3
myAPI='0F5QQ31B2ZECFJTA'
#from datetime import datetime
import time,board, adafruit_dht
http=urllib3.PoolManager()   
dhtDevice= adafruit_dht.DHT11(board.D23)   
while True:
        try:
            temperature_c = dhtDevice.temperature
            temperature_f = temperature_c * (9 / 5) + 32
            humidity = dhtDevice.humidity
#             temperature_c = 12
#             temperature_f = 30
#             humidity = 100
            link='https://api.thingspeak.com/update?api_key={0}&field1={1:0.1f}&field2={2:0.1f}'.format(myAPI,temperature_c,humidity)
            r=http.request('GET',link)
            print(r.status)
               
            time.sleep(10)
        except Exception as E:
            print(E)
            time.sleep(5)
