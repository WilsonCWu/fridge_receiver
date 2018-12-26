import time
import pyanova


pa = pyanova.PyAnova(debug=True)

def WarmUpAndMaintain(goalTemp):
  print("Starting heating and cooking process, with goal temperature of %s" % goalTemp)
  pa.set_temperature(goalTemp)
  pa.start_anova()
  while True:
    time.Sleep(10)
    curTemp = pa.get_current_temperature()
    print("Goal Temp: %s. Cur Temp: %s." % (goalTemp, curTemp))
    if abs(goalTemp-curTemp) < 3:
      break
  print("Temperature is ready")
# if __name__ == '__main__':
#   print '~~ pyanova demo ~~'
#   print '-- Initializing PyAnova object'
#   pa = pyanova.PyAnova(debug=True)
#   cmd_re = re.compile('^get|^stop|^set')
#   cmd_list = list(filter(lambda m: cmd_re.match(m), dir(pa)))
#   print '-- PyAnova object initialized'
#   print '-- Available commands:\n    %s'%'\n    '.join(cmd_list)
#   print '-- Type commands like: \'get_current_temperature()\' or \'set_temperature(42)\''
#   print '-- Type \'bye\' to end demo'
#   while True:
#     ri = raw_input('> ')
#     if ri.lower().startswith('bye'):
#       print 'cya.'
#       break
#     else:
#       print '< ' + eval('pa.'+ri)