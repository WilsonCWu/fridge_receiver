# Servo Control
import time
import smbus
import wiringpi
import RangeSensor

# for dispenser servo
wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(18, wiringpi.GPIO.PWM_OUTPUT)
wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)
wiringpi.pwmSetClock(192)
wiringpi.pwmSetRange(2000)
wiringpi.pwmWrite(18, 0)
dispenseTimeout = 20
# for RPI version 1, use "bus = smbus.SMBus(0)"
bus = smbus.SMBus(1)

# This is the address we setup in the Arduino Program
#Slave Address 1
address = 0x04

print("Ran init for servo")
RangeSensor.setup()

def DropFood():
  time.sleep(1)
  wiringpi.pwmWrite(18, 90)
  RangeSensor.WaitForDrop(dispenseTimeout)
  wiringpi.pwmWrite(18, 0)
def OpenDoor():
  print("Opening door")
  bus.write_byte(address, 1)

def CloseDoor():
  print("Closing door")
  bus.write_byte(address, 0)

def Quit():
  RangeSensor.Quit()