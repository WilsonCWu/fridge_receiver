import MySQLdb

f=open("passwords/mysql_username", "r")
username = f.read().rstrip()
f=open("passwords/mysql_password", "r")
password = f.read().rstrip()

db = MySQLdb.connect("localhost", username, password, "fridge")
curs=db.cursor()

def GetMessages():
  print("Getting SQL Messages")
  curs.execute("SELECT * FROM commands")
  commands = []
  for value in curs.fetchall():
    commands.append(value[2])
    deleteStr = "DELETE FROM commands WHERE date='%s' AND time='%s' AND command='%s'" % (str(value[0]), str(value[1]), value[2])
    curs.execute(deleteStr)
  db.commit()
  return commands
def Quit():
  