import DataQueue
import StepperMotor

cycleLength = 5
def run():
  print("Starting full process")
  StepperMotor.RotateMotorFullCircle()

def main():
  while True:
    messages = DataQueue.GetMessages()
    for message in messages:
      print("Message Received: " + message)
      if message == "run":
        run()

    time.sleep(cycleLength)

if __name__ == "__main__":
    main()