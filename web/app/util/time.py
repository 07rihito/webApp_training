import time
import datetime


def logMsg(msg):
  now = datetime.datetime.now()
  #print(now.strftime("%Y/%m/%d %H:%M:%S.%f"))
  print(now.strftime("%Y/%m/%d %H:%M:%S") + ": " + msg)
  #freturn now.strftime("%Y/%m/%d %H:%M:%S") + ": " + msg