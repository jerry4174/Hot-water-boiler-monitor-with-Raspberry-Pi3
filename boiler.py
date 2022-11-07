#!/usr/bin/env python3
# Recording of switching times for boiler, pump, heating etc.
# Author: Jerry  Date: 31.10.2022
# start program remote (putty): sudo nohup python ./boiler.py & -> PID
# stop program: kill PID

import time
import board
import busio
import adafruit_ads1x15.ads1115 as ADS		# import module for  ADS1115 board
from adafruit_ads1x15.analog_in import AnalogIn # import library for analog input
from datetime import datetime



i2c = busio.I2C(board.SCL, board.SDA) # create IC2 communication on SCL and SDA pins
ads = ADS.ADS1115(i2c)		      # create an ADS object 
boiler = "off"     # old status
boiler1 = "off"    # changed status 

chan = AnalogIn(ads, ADS.P0)  # create the analog input channel on ADS1115 board, pin A0

now = datetime.now()
filename = now.strftime("%d%m%H%M")+".log" # create a new log file
print (filename)


while True:            # Loop: program is running until kill
    
     now = datetime.now()
     dt_string = now.strftime("%Y.%m.%d %H:%M:%S") # date/time string
     volts = (str(round(chan.voltage,2))) # read rounded analog voltage to string
     #print volts
     time.sleep(30)       # wait for 30 seconds and read the voltage again
 
 # Threshold voltage is 2V here, depends on signal power supply.
 # The device is switched on:
     if float(volts) > 2 and boiler1 == "off":  
         print (" On,", dt_string)
         f = open(filename, "a") 
         f.write('On ' + dt_string + '\n')
         f.close()
         boiler = "on"
         boiler1 = "on"
 # The device is switched off:        
     elif float(volts) < 2 and boiler1 == "on":
         print ('Off,', dt_string)
         f = open(filename, "a") 
         f.write('Off ' + dt_string + '\n')
         f.close()
         boiler = "off"
         boiler1 = "off"
   
