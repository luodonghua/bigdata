#!/usr/bin/python

import threading
import time
import datetime
import random
import traceback
import syslog
import os
import socket

ExitFlag=False
Transactions=0
PreTransactions=0
batchname=datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')

print ("Batch Name: " + batchname)

class MyThread (threading.Thread):

    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name=name

    def run(self):
        global Transactions
        while not ExitFlag:
            try:

                logmsg = "TheadID: %s, BatchName: %s, Event Time: %s" % (self.name, batchname, datetime.datetime.now())

                # Method 1: using syslog package
                # syslog.openlog(logoption=syslog.LOG_PID, facility=syslog.LOG_LOCAL6)
                # syslog.syslog(syslog.LOG_INFO, logmsg)

                # Method 2: using OS logger command
                #os.system('logger -p auth.info ' + logmsg)

                # Method 3: using TCP socket
                # <38>Sep 22 08:05:27 sgc7hadclient1 root:
                # TheadID: Thread-0, BatchName: 2018-09-22T08:04:27, Event Time: 2018-09-22 08:05:27.909249

                syslogmsg = u"<38>%s %s %s:%s" %(datetime.datetime.now().strftime('%b %d %H:%M:%S'),os.uname()[1],os.getlogin(),logmsg)
                tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                tcpsock.connect(('localhost', 10001))
                tcpsock.send((syslogmsg + '\n').encode('raw-unicode-escape'))
                tcpsock.close()

                Transactions = Transactions +1
                time.sleep(1)
            except:
                #pass
                print(traceback.format_exc())
        print('Exiting ' + self.name)


ThreadList=[]
for i in range(0, 1): # simulate 2 applications
    ThreadList.append('Thread-'+str(i))
# ThreadList = ["Thread-1"]
threads = []

StarTime=datetime.datetime.now()

for t in ThreadList:
    thread=MyThread(t)
    thread.start()
    threads.append(thread)

StopMinutes=1
while datetime.datetime.now()-StarTime<datetime.timedelta(minutes=StopMinutes):
    print ('['+str(datetime.datetime.now())+'] TPS: '+str(Transactions-PreTransactions))
    PreTransactions=Transactions
    time.sleep(1)

ExitFlag=True

print ('['+str(datetime.datetime.now())+'] Total Message: '+str(Transactions))

for t in threads:
    t.join()

print ("Exiting Main Thread")