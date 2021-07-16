import sys
import socket
import binascii
import re
import libscrc
import json
import paho.mqtt.client as paho
import os

def twosComplement_hex(hexval):
    bits = 16
    val = int(hexval, bits)
    if val & (1 << (bits-1)):
        val -= 1 << bits
    return val

# CONFIG

inverter_ip="192.168.X.XXX"
inverter_port=8899
inverter_sn=17XXXXXXX
mqtt=1
mqtt_server="192.168.X.X"
mqtt_port=1883
mqtt_topic="XXXXXXXX"
mqtt_username=""
mqtt_passwd=""

# END CONFIG
os.chdir(os.path.dirname(sys.argv[0]))
# Initialise MQTT if configured

if mqtt==1: 
 client=paho.Client("inverter")
 if mqtt_username!="":  # only if mqtt_username is defined
  client.tls_set()  # <--- even without arguments
  client.username_pw_set(username=mqtt_username, password=mqtt_passwd)
 client.connect(mqtt_server, mqtt_port)

# PREPARE & SEND DATA TO THE INVERTER
output="{" # initialise json output
pini=0
chunks=0
while chunks<2:
 pfin=pini+100
 if chunks==-1: # testing initialisation
  pini=235
  pfin=235
  print("Initialise Connection")
 start = binascii.unhexlify('A5') #start
 length=binascii.unhexlify('1700') # datalength
 controlcode= binascii.unhexlify('1045') #controlCode
 serial=binascii.unhexlify('0000') # serial
 datafield = binascii.unhexlify('020000000000000000000000000000') #com.igen.localmode.dy.instruction.send.SendDataField
 pos_ini=str(hex(pini)[2:4].zfill(4))
 pos_fin=str(hex(pfin-pini+1)[2:4].zfill(4))
 businessfield= binascii.unhexlify('0103' + pos_ini + pos_fin) # sin CRC16MODBUS
 crc=binascii.unhexlify(str(hex(libscrc.modbus(businessfield))[4:6])+str(hex(libscrc.modbus(businessfield))[2:4])) # CRC16modbus
 checksum=binascii.unhexlify('00') #checksum F2
 endCode = binascii.unhexlify('15')
 
 inverter_sn2 = bytearray.fromhex(hex(inverter_sn)[8:10] + hex(inverter_sn)[6:8] + hex(inverter_sn)[4:6] + hex(inverter_sn)[2:4])
 frame = bytearray(start + length + controlcode + serial + inverter_sn2 + datafield + businessfield + crc + checksum + endCode)
 
 checksum = 0
 frame_bytes = bytearray(frame)
 for i in range(1, len(frame_bytes) - 2, 1):
     checksum += frame_bytes[i] & 255
 frame_bytes[len(frame_bytes) - 2] = int((checksum & 255))
 
 # OPEN SOCKET
 
 for res in socket.getaddrinfo(inverter_ip, inverter_port, socket.AF_INET,
                                            socket.SOCK_STREAM):
                  family, socktype, proto, canonname, sockadress = res
                  try:
                   clientSocket= socket.socket(family,socktype,proto);
                   clientSocket.settimeout(10);
                   clientSocket.connect(sockadress);
                  except socket.error as msg:
                   print("Could not open socket");
                   break
 
 # SEND DATA
 #print(chunks)
 clientSocket.sendall(frame_bytes);
 
 ok=False;
 while (not ok):
  try:
   data = clientSocket.recv(1024);
   ok=True
   try:
    data
   except:
    print("No data - Die")
    sys.exit(1) #die, no data
  except socket.timeout as msg:
   print("Connection timeout");
   sys.exit(1) #die
 
 # PARSE RESPONSE (start position 56, end position 60)
 
 i=pfin-pini
 a=0
 while a<=i:
  p1=56+(a*4)
  p2=60+(a*4)
  response=twosComplement_hex(str(''.join(hex(ord(chr(x)))[2:].zfill(2) for x in bytearray(data))+'  '+re.sub('[^\x20-\x7f]', '', ''))[p1:p2])
  hexpos=str("0x") + str(hex(a+pini)[2:].zfill(4)).upper()
  with open("./DYRealTime.txt") as txtfile:
   parameters=json.loads(txtfile.read())
  for parameter in parameters:
   for item in parameter["items"]:
     title=item["titleEN"]
     ratio=item["ratio"]
     unit=item["unit"]
     for register in item["registers"]:
      if register==hexpos and chunks!=-1:
       #print(title+":"+str(response*ratio)+unit)
       output=output+"\""+ title + "(" + unit + ")" + "\":" + str(response*ratio)+","
  a+=1
 pini+=100
 chunks+=1  
output=output[:-1]+"}"
if mqtt==1:
 client.publish(mqtt_topic,"Online")
 client.publish(mqtt_topic+"/attributes",output)
 print("Ok")
else:
 print(output)
