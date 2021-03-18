import RPi.GPIO as gpio
import time
import serial
import math
global ser
global ser2
ser = serial.Serial(
   port='/dev/ttyS0',
   baudrate = 9600,
   parity=serial.PARITY_NONE,
   stopbits=serial.STOPBITS_ONE,
   bytesize=serial.EIGHTBITS,
   timeout=1
)
while True:
       #p=pathlib.Path(path)
    try:
        line=ser.readline()
        print(line)
        line1=line.rstrip().decode()
        print(line1)
        with open("/home/pi/iot-batch2/dht11.txt","a+") as file:
            file.write(line1) 
    except Exception as e:
        print("error occured: ",e)

        