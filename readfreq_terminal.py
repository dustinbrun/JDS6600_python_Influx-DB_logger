
from jds6600 import jds6600
import warnings
import serial
import serial.tools.list_ports
import time

print("-----------------JDS6600-Reader-----------------")
print("Searching Device ...")

found_ports = [
    p.device
    for p in serial.tools.list_ports.comports()
    if 'CH340' in p.description or 'USB Serial' in p.description    #CH340 for Windows, USB Serial for Linux
]
if not found_ports:
    raise IOError("No JDS6600-device found")
if len(found_ports) > 1:
    warnings.warn('Multiple JDS6600-devices found - using the first')

portname = found_ports[0]
print("JDS6600 device found!")
print("Using Port ", portname)

jds = jds6600(portname)
#jds = jds6600("COM4")

print("--------------------------")
# API information calls
print("Devicetype: ", jds.getinfo_devicetype())
print("Serialnumber:", jds.getinfo_serialnumber())
print("--------------------------")

#Disable Both outputs
#print(jds.getchannelenable())
jds.setchannelenable(bool(0), bool(0))
print("Disabeling Outputs ... \t\t OK")

#print(jds.getmode())
jds.setmode('MEASURE')
print("Set Mode Measure ... \t\t OK")

jds.measure_setcoupling('AC')
jds.measure_setgate(1) #Gatetime 1s
jds.measure_setmode("PERIOD")
print("Configure Measurement ... OK")
print("--------------------------")

while 1:
    if jds.getmode()[0] != 4:   # 4 means mode 'MEASURE'
        raise IOError("Measurement-mode is not enabled!")
    print(jds.measure_getfreq_p())
    time.sleep(1)

