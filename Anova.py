import time
import sys
import pyanova
import subprocess

def WarmUpAndMaintain(goalTemp):
  while True:
    try:
      print("Starting heating and cooking process, with goal temperature of %s" % goalTemp)
      pa = pyanova.PyAnova(debug=True)
      print("Connected to anova")
      pa.set_temperature(goalTemp)
      pa.start_anova()
      while True:
        time.sleep(5)
        curTemp = float(pa.get_current_temperature())
        print("Goal Temp: %s. Cur Temp: %s." % (goalTemp, curTemp))
        if abs(goalTemp-curTemp) < 3:
          break
      print("Temperature is ready")
    except KeyboardInterrupt:
      subprocess.call(['./AnovaReset.sh'])
      sys.exit()
    except:
      subprocess.call(['./AnovaReset.sh'])
      continue
    break
def Quit():
  subprocess.call(['./AnovaReset.sh'])