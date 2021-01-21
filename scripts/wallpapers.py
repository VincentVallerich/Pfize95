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
    return "C:\\" in str(platform)

def path():
    return "C:\\" if "C:\\" in str(platform) else "/"


def change_wallpaper(path):
    while True:
        for dirpath, dirnames, filenames in os.walk(path):
            for filename in [f for f in filenames if f.endswith(".png") or f.endswith(".jpg") or f.endswith(".jpeg")]:
                try:
                    if isWindows():
                        ctypes.windll.user32.SystemParametersInfoW(20, 0, os.path.join(dirpath, filename) , 0)
                    else:
                        os.system("/usr/bin/gsettings set org.gnome.desktop.background picture-uri " + os.path.join(dirpath, filename))
                    time.sleep(0.1)
                except:
                    continue


change_wallpaper(path())
