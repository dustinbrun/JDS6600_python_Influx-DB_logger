import os
import serial.tools.list_ports

ports = serial.tools.list_ports.comports(include_links=True)

print("Serial Ports:")
print("path \t\t| name \t\t| description")
print("-------------------------------------------------------------------------")

for port in ports :
    print(port.device + " \t\t| " + port.name + "\t\t| " + port.description)

print("-------------------------------------------------------------------------")

os.system("pause")
    