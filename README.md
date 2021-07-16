# DeyeInverter
Small utility to read data from DEYE Inverters through the Solarman Datalogger. Works with S/N 17*

MQTT support into Home Assistant:

```
  - platform: mqtt
    name: "DeyeInverter"
    state_topic: "mqtt_topic"
    json_attributes_topic: "mqtt_topic/attributes"
```

Thanks to @fjcarretero https://github.com/fjcarretero for his incredible support on understanding the data from and to the datalogger.
Thanks to @xtheone https://github.com/XtheOne for his original V4 reader that was an inspiration (and I borrowed *some* code).

# Configuration

Edit the InverterData.py and enter the following data:
```
inverter_ip="192.168.X.XXX"
inverter_port=8899
inverter_sn=17XXXXXXXX
mqtt=1
mqtt_server="192.168.X.X"
mqtt_port=1883
# this script will output data in 2 topics for Home Assistant, feel free to modify it to your needs
# Status will be output into the mqtt_topic
# attributes will be output in mqqt_topic/attributes
mqtt_topic="XXXXXXXXXXX"
```

# Run

```python3 InverterData.py

{"Inverter ID()":XXXXX,
"Inverter ID()":XXXXX,
"Inverter ID()":XXXXX,
"Inverter ID()":XXXXX,
"Inverter ID()":XXXXX,
"Control Board Version No.()":12642,
"Communication Board Version No.()":-31926,
"Running Status()":2,
"Total Grid Produciton(kwh)":829.5,
"Total Grid Produciton(kwh)":0.0,
"Daily Energy Bought(kwh)":0.0,
"Daily Energy Sold(kwh)":15.0,
"Total Energy Bought(kwh)":21.900000000000002,
"Total Energy Bought(kwh)":0.0,
"Total Energy Sold(kwh)":1103.4,
"Total Energy Sold(kwh)":0.0,
"Daily Load Consumption(KWH)":1.2000000000000002,
"Total Load Consumption(KWH)":365.3,
"Total Load Consumption(KWH)":0.0,
"DC Temperature(℃)":149.5,
"AC Temperature(℃)":152.1,
"Total Production(KWH)":1517.4,
"Total Production(KWH)":0.0,
"Alert()":0,
"Alert()":0,
"Alert()":0,
"Alert()":0,
"Alert()":0,
"Alert()":0,
"Daily Production(KWH)":16.900000000000002,
"PV1 Voltage(V)":342.20000000000005,
"PV1 Current(A)":7.800000000000001,
"PV2 Voltage(V)":8.5,
"PV2 Current(A)":0.0,
"Grid Voltage L1(V)":241.3,
"Grid Voltage L2(V)":0.0,
"Load Voltage(V)":242.9,
"Current L1(A)":10.51,
"Current L2(A)":0.0,
"Micro-inverter Power(W)":0,
"Gen-connected Status()":0,
"Gen Power(W)":0,
"Internal CT L1 Power(W)":-2325,
"Internal CT L2  Power(W)":0,
"Grid Status()":-2365,
"Total Gird Power(W)":-2365,
"External CT L1 Power(W)":-2365,
"External CT L2 Power(W)":0,
"Inverter L1 Power(W)":2558,
"Inverter L2 Power(W)":0,
"Total Power(W)":2558,
"Load L1 Power(W)":193,
"Load L2 Power(W)":0,
"Total Load Power(W)":193,
"Battery Temperature(℃)":125.0,
"Battery Voltage(V)":10.14,
"Battery SOC(%)":0,
"PV1 Power(W)":2619,
"PV2 Power(W)":0,
"Battery Status()":0,
"Battery Power(W)":0,
"Battery Current(A)":-0.01,
"Grid-connected Status()":1,
"SmartLoad Enable Status()":16}
```

# Known Issues

Some data seems to be out of scale, for example all Temperatures are shown +100ºC.

# Contrib

Python is not my strongest suite, feel free to suggest, rewrite or add whatever you feel is necessary.


