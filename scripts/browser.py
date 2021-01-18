import webbrowser as wb
import time

import psutil
def checkIfProcessRunning(processName):
    '''
    Check if there is any running process that contains the given name processName.
    '''
    #Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;





def openWeb():
    file = open("links.txt", "r")
    txt=file.readline()
    wb.open_new(txt)
    while True:
        if txt=="STOP":
            file.seek(0,0)
            txt=file.readline()
        elif not (checkIfProcessRunning("chrome") or checkIfProcessRunning("edge") or checkIfProcessRunning("firefox")):
            wb.open_new(txt)
            txt=file.readline()

openWeb()