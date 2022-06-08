import string
import os
import psutil

def myFunc1(imie:str):
    if imie == "Szymix":
        os.system("shutdown /s /t 1")

def checkBaterry():
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = str(battery.percent)
    plugged = "Plugged In" if plugged else "Not Plugged In"
    print(percent+'% | '+plugged)
