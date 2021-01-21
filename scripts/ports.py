import pip
import sys


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


require('socket', 'threading')


from socket import *
from threading import *


def ecouter(port):
    """masocket = socket(AF_INET, SOCK_STREAM)
    masocket.bind((gethostname(), port))"""
    print("coucou1")
    """masocket.listen(5)
    masocket.accept()"""
    print("coucou2")



def lancer():
    while True:
        for port in range(65535):
            monThread = Thread(ecouter(port))
            monThread.start()


def portsOuverts():
    masocket = socket(AF_INET, SOCK_STREAM)
    for port in range(65535):
        resultat = masocket.connect_ex((gethostname(), port))
        if resultat == 0:
            print("Port is open")
        """else:
            print("Port is closed")"""


portsOuverts()
lancer()
portsOuverts()

