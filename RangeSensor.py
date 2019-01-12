import RPi.GPIO as GPIO
import time

trigPin = 16
echoPin = 18
MAX_DISTANCE = 220          #define the maximum measured distance
timeOut = MAX_DISTANCE*60   #calculate timeout according to the maximum measured distance

closeDist = 20

def WaitForDrop(dispenseTimeout):
  t0 = time.time()
  while(getSonar() > closeDist):
    if((time.time() - t0) > dispenseTimeout):
      return;
    time.sleep(0.01)
  while(getSonar() < closeDist):
    if((time.time() - t0) > dispenseTimeout):
      return;
    time.sleep(0.01)
  time.sleep(1)


def pulseIn(pin,level,timeOut): # function pulseIn: obtain pulse time of a pin
  t0 = time.time()
  while(GPIO.input(pin) != level):
    if((time.time() - t0) > timeOut*0.000001):
      return timeOut;
  t0 = time.time()
  while(GPIO.input(pin) == level):
    if((time.time() - t0) > timeOut*0.000001):
      return timeOut;
  pulseTime = (time.time() - t0)*1000000
  return pulseTime
    
def getSonar():     #get the measurement results of ultrasonic module,with unit: cm
  GPIO.output(trigPin,GPIO.HIGH)      #make trigPin send 10us high level 
  time.sleep(0.00001)     #10us
  GPIO.output(trigPin,GPIO.LOW)
  pingTime = pulseIn(echoPin,GPIO.HIGH,timeOut)   #read plus time of echoPin
  distance = pingTime * 340.0 / 2.0 / 10000.0     # the sound speed is 340m/s, and calculate distance
  return distance
    
def setup():
  GPIO.setmode(GPIO.BOARD)       #numbers GPIOs by physical location
  GPIO.setup(trigPin, GPIO.OUT)   #
  GPIO.setup(echoPin, GPIO.IN)    #
  print ('Range Sensor setup complete')

def Quit():
  GPIO.cleanup()

