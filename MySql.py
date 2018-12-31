import MySQLdb

f=open("passwords/mysql_username", "r")
username = f.read().rstrip()
f=open("passwords/mysql_password", "r")
password = f.read().rstrip()

db = MySQLdb.connect("localhost", username, password, "fridge")
curs=db.cursor()

def GetMessages():
  curs.execute("SELECT * FROM commands")
  commands = []
  print "\nDate       Time    Command"
  print "============================"
  for value in curs.fetchall():
    commands.append(value[2])
    deleteStr = "DELETE FROM commands WHERE date='%s' time='%s' command='%s'" % (str(value[0]), str(value[1]), value[2])
    print(deleteStr)
    curs.execute(deleteStr)
    print str(value[0])+" "+str(value[1])+"   "+value[2]
  return commands
