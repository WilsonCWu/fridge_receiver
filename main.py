import time
import Init
import DataQueue
import StepperMotor
import Anova

cycleLength = 5
targetTemp = 70.0

def heatWater():
  Anova.WarmUpAndMaintain(targetTemp)

def dispenseFood():
  StepperMotor.RotateMotorFullCircle()

def run():
  print("Starting full process")
  heatWater()
  dispenseFood()

def main():
  while True:
    messages = DataQueue.GetMessages()
    for message in messages:
      print("Message Received: " + message)
      if message == "run" or message == "Run":
        run()
      elif message == "cook" or message == "Cook":
        heatWater()
      elif message == "dispense" or message == "Dispense":
        dispenseFood()

    time.sleep(cycleLength)
  StepperMotor.Quit()

if __name__ == "__main__":
    main()
