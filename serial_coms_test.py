from serial_coms import serialLine

microController = serialLine(38400) # Sets up serial communication line to STM32 (9600 baud)

microController.sendDataBytes(100, 100, 
    300, 100, 100, 100)