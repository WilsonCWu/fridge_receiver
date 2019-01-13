import time
import Init
import DataQueue
import MySql
import Servo
import Anova

cycleLength = 1
targetTemp = 183

def openDoor():
  Servo.OpenDoor()

def closeDoor():
  Servo.CloseDoor()

def heatWater():
  Anova.WarmUpAndMaintain(targetTemp)

def dropFood():
  Servo.DropFood()

def dispenseFood():
  openDoor()
  time.sleep(0.5)
  dropFood()
  time.sleep(2)
  closeDoor()
  time.sleep(1)

def run():
  print("Starting full process")
  heatWater()
  dispenseFood()

def loop():
  while True:
    print("Running main loop")
    messages = MySql.GetMessages()
    #messages2 = DataQueue.GetMessages()
    #messages += messages2
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
def main():
  try:
    loop()
  except KeyboardInterrupt:  #when 'Ctrl+C' is pressed, the program will exit
    DataQueue.Quit()
    MySql.Quit()
    Servo.Quit()
    Anova.Quit()

if __name__ == "__main__":
    main()
