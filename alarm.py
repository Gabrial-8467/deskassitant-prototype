import datetime
from playsound import playsound
import time

def addalarms():
    alarmhour = int(input("Enter Hour: "))
    alarmmin = int(input("Enter min: "))
    alarmtime = input("am/pm: ")

    if alarmtime == "pm":
        alarmhour += 12

    return alarmhour, alarmmin

def playalarm(alarmhour, alarmmin):
    while True:
        current_time = datetime.datetime.now()
        print(f"Current Time: {current_time.hour}:{current_time.minute}")
        print(f"Alarm Time: {alarmhour}:{alarmmin}")

        if alarmhour == current_time.hour and alarmmin == current_time.minute:
            print("Playing...")
            playsound("sound\\alarmsound.wav")
            break

        time.sleep(30)  # Add a delay to reduce CPU usage (check every 30 seconds)

# Add alarms and then play them

