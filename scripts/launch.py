import os, sys, fnmatch, threading

def main():
    windows = False
    threads = []
    files = fnmatch.filter(os.listdir('.'), '*.py')
    for file in files:
        if file != "launch.py":
            t = threading.Thread(target=execute(file, windows))
            threads.append(t)
            t.start()

def execute(file, windows):
    if not windows:
        os.system("chmod +x " + file)
    os.system("python " + file)

if __name__ == "__main__":
    main()
