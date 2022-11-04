# Hot-water-boiler-monitor

## Description:
The python application **boiler.py** checks the status (switch-on, switch-off) of an electric device like boiler, heating or pump.  
The results are listed in a logfile:  

 On 2022.11.03 05:40:54  
Off 2022.11.03 05:54:35  
 On 2022.11.03 11:41:59  
Off 2022.11.03 11:57:52  
 On 2022.11.03 18:34:59  
Off 2022.11.03 18:48:45  

## Purpose:
For a system with an electric heating or hot water boiler in combination with Solar PV.  
If you know the frequency and lenghts of switch-on phases, you can then save money with better control of your PV system.
For example not to feed a boiler the whole night, but switch it on in suffiecient time before you need a hot water.

## Used Hardware:  
- Some power supply with DC voltage from 3V up to 5V. I have used an old clasical Nokia power supply with 3,7V.  
- Analog-to-digital converter ADS1115.   
- Raspberry Pi3.  

You find a simple wiring diagram in the Wiki.

             ![image](https://user-images.githubusercontent.com/117408439/200044270-70fd90e7-7197-4d1b-8cf9-ca227804f77e.png)


