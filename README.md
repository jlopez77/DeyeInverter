# DeyeInverter
Small utility to read data from DEYE Inverters through the Solarman Datalogger. Works with S/N 17*

Thanks to @fjcarretero https://github.com/fjcarretero for his incredible support on understanding the data from and to the datalogger.
Thanks to @xtheone https://github.com/XtheOne for his original V4 reader that was an inspiration (and I borrowed *some* code).

# Configuration

Edit the InverterData.py and enter the following data:
```
inverter_ip="192.168.X.XXX"
inverter_port=8899
inverter_sn=17XXXXXXXX
```

# Run

```python3 InverterData.py

Inverter ID:XXXXX
Inverter ID:XXXXX
Inverter ID:XXXXX
Inverter ID:XXXXX
Inverter ID:XXXXX
Control Board Version No.:8537
Communication Board Version No.:-31929
Running Status:2
Total Grid Produciton:145.3kwh
Total Grid Produciton:0.0kwh
Daily Energy Bought:8.700000000000001kwh
Daily Energy Sold:0.0kwh
Total Energy Bought:63.7kwh
Total Energy Bought:0.0kwh
Total Energy Sold:28.400000000000002kwh
Total Energy Sold:0.0kwh
Daily Load Consumption:12.9KWH
Total Load Consumption:183.0KWH
Total Load Consumption:0.0KWH
DC Temperature:165.3℃
AC Temperature:152.9℃
Total Production:157.0KWH
Total Production:0.0KWH
Alert:0
Alert:0
Alert:0
Alert:0
Alert:0
Alert:0
Daily Production:4.4KWH
PV1 Voltage:221.0V
PV1 Current:4.6000000000000005A
PV2 Voltage:216.5V
PV2 Current:8.1A
Grid Voltage L1:240.0V
Grid Voltage L2:0.0V
Load Voltage:248.10000000000002V
Current L1:5.17A
Current L2:0.0A
Micro-inverter Power:0W
Gen-connected Status:0
Gen Power:0W
Internal CT L1 Power:-1168W
Internal CT L2  Power:0W
Grid Status:53
Total Gird Power:53W
External CT L1 Power:53W
External CT L2 Power:0W
Inverter L1 Power:1145W
Inverter L2 Power:0W
Total Power:1145W
Load L1 Power:1198W
Load L2 Power:0W
Total Load Power:1198W
Battery Temperature:129.0℃
Battery Voltage:54.19V
Battery SOC:67%
PV1 Power:1018W
PV2 Power:1729W
Battery Status:-1547
Battery Power:-1547W
Battery Current:-28.55A
Grid-connected Status:1
SmartLoad Enable Status:16
```

# Known Issues

Some data seems to be out of scale, for example all Temperatures are shown +100ºC

# Contrib

Python is not my strongest suite, feel free to suggest, rewrite or add whatever you feel is necessary.


