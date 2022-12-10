# Hot-water-boiler-monitor

## Project Description
The python application **boiler.py** running in Raspberry Pi3 checks the status (switch-on, switch-off) of an electric device like boiler, heating or pump.  
The results are listed in a logfile:  

 On 2022.11.03 05:40:54  
Off 2022.11.03 05:54:35  
 On 2022.11.03 11:41:59  
Off 2022.11.03 11:57:52  
 On 2022.11.03 18:34:59  
Off 2022.11.03 18:48:45  

## Purpose
For a system with an electric heating or hot water boiler in combination with Solar PV.  
If you know the frequency and lenghts of switch-on phases, you can then save money with better control of your PV system.
For example you don't need to feed a boiler the whole night, but switch it on in suffiecient time before you use a hot water.

## Built With  
- Some power supply with DC output voltage from 3V up to 5V. I have used an old clasical Nokia power supply with 3.7V.  
- Analog-to-digital converter ADS1115.   
- Raspberry Pi3.  

## Getting Started
You find a an [electrical schematic](https://github.com/jerry4174/Hot-water-boiler-monitor/wiki/Electrical-Schematic) and [wiring diagram](https://github.com/jerry4174/Hot-water-boiler-monitor/wiki/Wiring-Diagram) in the Wiki.

## Installation
The monitor installation is described in the Wiki part [Installation Instructions](https://github.com/jerry4174/Hot-water-boiler-monitor/wiki/Installation-Instructions).

## Usage
- Switch off the boiler. Connect the monitor power supply to a boiler or a pump.  
- Use L and N wire. This job must be done by a licensed electrician.  
- Switch on the boiler
- Start remote boiler.py: sudo nohup python ./boiler.py & 
- Run the monitor about one week. After one week the log file will be evalueted. You will see the switching intervals of your boiler or another machine.
- Example of a log file: [log](https://github.com/jerry4174/Hot-water-boiler-monitor/blob/main/boiler%20log.JPG)



## License 
Distributed under the MIT License. See https://en.wikipedia.org/wiki/MIT_License for more information.



