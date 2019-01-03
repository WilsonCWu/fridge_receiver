# Servo Control
import time
import smbus

# for RPI version 1, use "bus = smbus.SMBus(0)"
bus = smbus.SMBus(1)

# This is the address we setup in the Arduino Program
#Slave Address 1
address = 0x04

print("Ran init for servo")

def OpenDoor():
  print("Opening door")
  bus.write_byte(address, 1)

def CloseDoor():
  print("Closing door")
  bus.write_byte(address, 0)
