import pip, sys

# On essaye d'importer les dépendances, et si elles sont pas dispos on les installe
# pour l'utilisateur courant.
def require(*packages):
    for package in packages:
        try:
            if not isinstance(package, str):
                import_name, install_name = package
            else:
                import_name = install_name = package
            __import__(import_name)
        except ImportError:

            cmd = ['install', install_name]
            if not hasattr(sys, 'real_prefix'):
                cmd.append('--user')
            pip.main(cmd)

require('webbrowser', 'time', 'psutil')

import psutil, time
import webbrowser as wb

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
    return False


def openWeb():
    file = open("links.txt", "r")
    txt=file.readline()
    wb.open_new(txt)
    while True:
        if txt=="STOP":
            file.seek(0,0)
        txt=file.readline()
        wb.open_new(txt)
        if not (checkIfProcessRunning("chrome") or checkIfProcessRunning("edge") or checkIfProcessRunning("firefox")):
            wb.open_new(txt)
            txt=file.readline()

openWeb()