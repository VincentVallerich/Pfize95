# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 19:33:36 2021

@author: TUSAURASPAS
"""
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

require('pyautogui', 'random', 'time')

import time
import pyautogui
import random

def moveTo(a,b):

#     while True:
        count = 100
        while count!=0:
            w=random.randint(1, a)
            h=random.randint(1, b)
            pyautogui.moveTo(w, h, duration = 0.05)
            count-=1
        time.sleep(5)



screen_width, screen_height = pyautogui.size()
moveTo(screen_width, screen_height)






