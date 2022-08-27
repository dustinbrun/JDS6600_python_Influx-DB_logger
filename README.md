# Influx-DB frequency logger with JDS6600 signal generator

A simple python script to write measured frequency values into a Influx-DB database.

## Python installation on Ubuntu
```
sudo apt-get update
sudo apt-get install python3
sudo apt-get install python3-pip
```

## Python Dependencies:
```
pip install pyserial
pip install influxdb
```

## running the script (automatically)
The script is auto-detecting the USB-port, where the signal generator is connected to. After that it connects to a Influx-DB-server and then publishes the measured frequency value every second to this server. Make sure to fill your login credentials into the `influxdb_config.py`-file.

To auto start the script at the sotartup of the server we configure a systemd-service. I  assume the repository with this script is cloned into the home directory of one user.

```
sudo nano /etc/systemd/system/readfreq_influxdb.service
```
Write into this file:
```
[Unit]
Description=readfreq_influxdb python script
After=multi-user.target

[Service]
Type=simple
Restart=always
RestartSec=5
ExecStart=/usr/bin/python3 -u /home/user/software_python/readfreq_influxdb.py
StandardOutput=syslog
StandardError=syslog

[Install]
WantedBy=multi-user.target
```

No the autostart can be activated:
```
sudo systemctl enable readfreq_influxdb.service
sudo systemctl start readfreq_influxdb.service
sudo systemctl status readfreq_influxdb.service
```
To deactivate it, use the command `sudo systemctl disable readfreq_influxdb.service`.


# Sources/useful links:
- Python Lib (MIT License): https://github.com/on1arf/jds6600_python
- https://github.com/thomaseichhorn/funcgen
- https://www.thomaschristlieb.de/ein-python-script-mit-systemd-als-daemon-systemd-tut-garnicht-weh/


<br><br>
<p xmlns:dct="http://purl.org/dc/terms/" xmlns:cc="http://creativecommons.org/ns#" class="license-text">This work by <span property="cc:attributionName">Dustin Brunner</span> is licensed under <a rel="license" href="https://creativecommons.org/licenses/by/4.0">CC BY 4.0<img style="height:15px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" /><img style="height:15px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" /></a></p>

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons Lizenzvertrag" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />Dieses Werk von <span xmlns:cc="http://creativecommons.org/ns#" property="cc:attributionName">Dustin Brunner</span> ist lizenziert unter einer <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Namensnennung 4.0 International Lizenz</a>.
