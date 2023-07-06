# Ant to Serial

RPi-based ANT+ Dongle to UART Bridge used to collect data from the heart rate monitor and power pedals each rider has and feed it to our data system over serial (UART) connection.

# Operation

The RPi is configured to boot this system automatically when powered by executing the `ant_startup.py` script when booted (done by editing [rc.local](https://linuxhint.com/use-etc-rc-local-boot/)). The RPis are configured to boot to command line (CLI) rather than starting the graphical user interface since there is no need for it in this project and we believe this also slightly improves the speed of the system to boot.

`ant_startup.py` then launches a series of other processes that collectively represent the ANT system.

- `power_off.py` is launched to watch for a press of the 'OFF' button and react accordingly
- `ant_bridge.py` is the actual ant bridge code
  
Once these are running, the startup script then responsible for determining whether the RPi is supposed to be the front or rear rider's system based on the presence or absence (respectively) of an ANT+ reciever, and launching the overlay program, `bike.bin`, accordingly by passing it the right arguements. 

- `serialComs` - Responsible for handling communication with the STM32
