# Servo Control
import time
import wiringpi
 
# use 'GPIO naming'
wiringpi.wiringPiSetupGpio()
 
# set #18 to be a PWM output
wiringpi.pinMode(18, wiringpi.GPIO.PWM_OUTPUT)
 
# set the PWM mode to milliseconds stype
wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)
 
# divide down clock
wiringpi.pwmSetClock(192)
wiringpi.pwmSetRange(2000)
 
delay_period = 3
hinge_closed = 200
hinge_opened = 130
wedge_closed = 180
wedge_opened = 90
wiringpi.pwmWrite(18, closed_position)

print("Ran init for servo")

def OpenDoor():
  print("Opening door")
  #wiringpi.pwmWrite(18, hinge_opened)
  #time.sleep(delay_period)

def CloseDoor():
  print("Closing door")
  #wiringpi.pwmWrite(18, hinge_closed)
  #time.sleep(delay_period)
