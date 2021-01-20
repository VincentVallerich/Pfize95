import os, sys, fnmatch, threading, multiprocessing, subprocess

def main():
    windows = False
    files = fnmatch.filter(os.listdir('.'), '*.py')
    for file in files:
        if file != "launch.py":
            os.chmod(file, 0o777)
            p = subprocess.Popen(["python3", file])

main()
