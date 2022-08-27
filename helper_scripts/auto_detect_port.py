import warnings
import serial
import serial.tools.list_ports

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
print(portname)