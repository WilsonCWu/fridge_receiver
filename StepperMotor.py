import RPi.GPIO as GPIO
import time

control_pins = [16,18,22,32]

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)


for pin in control_pins:
  GPIO.setup(pin, GPIO.OUT)
  GPIO.output(pin, 0)

halfstep_seq = [
  [1,0,0,0],
  [1,1,0,0],
  [0,1,0,0],
  [0,1,1,0],
  [0,0,1,0],
  [0,0,1,1],
  [0,0,0,1],
  [1,0,0,1]
]
print("Ran init for motor")
def RotateMotorFullCircle():
  print("Rotating motor")
  for i in range(512):
    for halfstep in range(8):
      for pin in range(4):
        GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
      time.sleep(0.001)

