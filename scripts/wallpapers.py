# import pip, sys
# # On essaye d'importer les dépendances, et si elles sont pas dispos on les installe
# # pour l'utilisateur courant.
# def require(*packages):
#     for package in packages:
#         try:
#             if not isinstance(package, str):
#                 import_name, install_name = package
#             else:
#                 import_name = install_name = package
#             __import__(import_name)
#         except ImportError:
#
#             cmd = ['install', install_name]
#             if not hasattr(sys, 'real_prefix'):
#                 cmd.append('--user')
#             pip.main(cmd)
#
# require('commands')

import ctypes, platform, os, time


def isWindows():
    return "win" in platform


def change_wallpaper(path):
    extensions = ["jpg", "png"]
    while True:
        for i in os.listdir(path):
            try:
                if i.split(".")[1] in extensions:
                    if isWindows():
                        ctypes.windll.user32.SystemParametersInfoW(20, 0, "C:\\Cybersecu\\images\\" + i , 0)
                    else:
                        os.system("/usr/bin/gsettings set org.gnome.desktop.background picture-uri /tmp/Cybersecu/images/" + i)
                    time.sleep(0.2)
            except:
                continue


change_wallpaper("./images")
