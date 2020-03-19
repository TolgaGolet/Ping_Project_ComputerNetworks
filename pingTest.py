from datetime import datetime
import time, os

#python -u pingTest.py >> log.txt          -u means unbuffered, >> means append

testTimes = ["18:00", "20:00", "22:00", "00:00"]
numberOfPings = 100
destinations = [["Twitter", "104.244.42.193"], ["Instagram", "34.234.250.88"], ["Habertürk", "92.45.106.101"], ["Yahoo", "72.30.35.9"], ["Sabah", "167.99.16.180"], ["Twitch", "151.101.66.167"], ["YouTube", "172.217.169.142"], ["Ticaret.edu.tr", "88.255.149.200"], ["Facebook", "72.52.179.174"], ["Nvidia", "216.228.121.209"]]

now = datetime.now()
print("**************************************************************************************Day")
print("@Test initialized on", now.strftime("%d-%m-%Y %A %H:%M:%S"))

while True:
    now = datetime.now()
    currentTime = now.strftime("%H:%M")
    print(" Time:", currentTime)
    if currentTime in testTimes:
        print(" Ping test started on", currentTime)
        i = 1
        for server in destinations:
            print(" " + str(i) + "-----Pinging " + server[0] + " (" + server[1] + ")")
            command = "ping -n " + str(numberOfPings) + " " + server[1]
            os.system(command)
            i+=1
            print(" ----------------------------------------------------------------------Destination")
        now = datetime.now()
        currentTime = now.strftime("%H:%M")
        print(" Ping test finished on", currentTime)
    else:
        print("Waiting for the next pinging time...")
        time.sleep(60)
