# First Thanks...

 + ...to @jlopez77 https://github.com/jlopez77

This is a fork from jlopez77/DeyeInverter

 + ... to @fjcarretero https://github.com/fjcarretero 

 + ...to @xtheone https://github.com/XtheOne 

for the initial work and code in the origin Repo

and aswell  
 + ...to @jmccrohan https://github.com/jmccrohan for his lighwight Solarman Scan utility!


## DeyeInverter

Small utility to read data from DEYE Micro Inverters with integrated Wifi Modules.through the Solarman Datalogger. 

Tests indicate that the full ModBus is available through the TCP connection. 

**Probably** this *can lead* to modifying Inverter Configuration via TCP calls.


## Tested and works with 

Deye SUN800G3-EU-230 Micro Inverters
+ Logger SN: 41xxxxxxxx
+ Inverter SN: 22xxxxxxxx


### Scan for Logger

```
python3.x deye_scan.py
```


### Configuration

Edit the deyeconfig.cfg and enter the following data:
```
[DeyeInverter]
inverter_ip=192.168.X.XXX
inverter_port=8899
inverter_sn=41xxxxxxxx
installed_power=XXXXX #power in Watts e.g. for 4.5kW write 4500
```


### Run

```
python3.x InverterData.py
```

```
{
    "Running Status()":4,
    "Daily Production(kWh)":0.1,
    "Total Production(kWh)":3.3,
    "Total Production 1(kWh)":1.6,
    "Total Production 2(kWh)":1.6,
    "AC Voltage(V)":234.0,
    "Total AC Output Current(A)":0.1,
    "AC Output Frequency(Hz)":50.1,
    "Total AC Output Power (Active)(W)":30.0,
    "Inverter Temperature(Cº)":12.2,
    "PV1 Voltage(V)":26.0,
    "PV1 Current(A)":0.5,
    "PV2 Voltage(V)":28.2,
    "PV2 Current(A)":0.5,
    "Grid Voltage Upper Limit(V)":275.0,
    "Grid Voltage Lower Limit(V)":180.0,
    "Grid Frequency Upper Limit(Hz)":52.0,
    "Grid Frequency Lower Limit(Hz)":47.5,
    "Installed Power(W)":3.8
}
```


### Use with Domoticz

Create Virtual Devices in Domoticz (look at domoticz_sample.config) 

and let the Script run every 5 minutes. (Example with Cron)


## Known Issues

The inverter is not fast enough to answer, you can get timeouts if you query it too often.


## Contrib

Python is not my strengh - also the BASH Script wont be the nicest, both both do its work. 
