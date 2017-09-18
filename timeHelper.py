import time

class TimeHelper(object):

 def __init__(self):
     time_bot_init = time.localtime()
     time_last_order = time.localtime()



 def printLocalTime(self,localTime):
     localTime_printable = "[{}.{}.{} | {}:{}]".format(
        localTime.tm_year, localTime.tm_mon, localTime.tm_mday, localTime.tm_hour, localTime.tm_sec)
     print(localTime_printable)