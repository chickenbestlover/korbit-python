import time

class TimeHelper(object):

 def __init__(self):

     self.time_bot_init = time.localtime()
     self.time_last_bidOrder = time.localtime()
     self.time_last_askOrder = time.localtime()

     self.bidOrderCount = 0
     self.askOrderCount = 0

 def tick(self):
     time.sleep(1)
     self.localTime = time.localtime()
     self.printStatus()

 def time2string(self,structTime):
     structTime_printable = "[{}.{}.{} | {}:{}]".format(
         structTime.tm_year, structTime.tm_mon, structTime.tm_mday, structTime.tm_hour, structTime.tm_sec)
     return structTime_printable

 def printableLocalTime(self):
     return self.time2string(self.localTime)

 def timeConnected(self):
     return time.mktime(self.localTime) - time.mktime(self.time_bot_init)

 def timeFromLastBidOrder(self):
     return time.mktime(self.localTime) - time.mktime(self.time_last_bidOrder)

 def record(self, ordertype='bid'):
     if ordertype == 'bid':
         self.bidOrderCount +=1
         self.time_last_bidOrder = time.localtime()
     elif ordertype == 'ask':
         self.askOrderCount += 1
         self.time_last_askOrder = time.localtime()

 def printStatus(self):
     timeConnected = self.timeConnected()

     if timeConnected % 600 == 0:
         localTime = self.time2string(self.localTime)
         print(localTime+'# of bid order: ' + str(self.bidOrderCount) + ' | # or ask order : '+str(self.askOrderCount))
