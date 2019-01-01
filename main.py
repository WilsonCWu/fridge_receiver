import time
import Init
import DataQueue
import MySql
import StepperMotor
import Servo
import Anova


cycleLength = 5
targetTemp = 70.0

def openDoor():
  Servo.OpenDoor()

def closeDoor():
  Servo.CloseDoor()

def heatWater():
  Anova.WarmUpAndMaintain(targetTemp)

def dropFood():
  StepperMotor.RotateMotorFullCircle()

def dispenseFood():
  openDoor()
  time.sleep(3)
  dropFood()
  time.sleep(3)
  closeDoor()
  time.sleep(3)

def run():
  print("Starting full process")
  heatWater()
  dispenseFood()

def main():
  while True:
    messages = DataQueue.GetMessages()
    messages2 = MySql.GetMessages()
    messages += messages2
    for message in messages:
      print("Message Received: " + message)
      if message == "run" or message == "Run":
        run()
      elif message == "cook" or message == "Cook":
        heatWater()
      elif message == "dispense" or message == "Dispense":
        dispenseFood()
      elif message == "openDoor" or message == "OpenDoor":
        openDoor()
      elif message == "closeDoor" or message == "CloseDoor":
        closeDoor()
      elif message == "drop" or message == "Drop":
        dropFood()

    time.sleep(cycleLength)
  StepperMotor.Quit()

if __name__ == "__main__":
    main()
