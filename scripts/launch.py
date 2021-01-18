import os, sys, fnmatch, threading, multiprocessing, subprocess

def main():
    windows = False
    files = fnmatch.filter(os.listdir('.'), '*.py')
    for file in files:
        if file != "launch.py":
            p = subprocess.Popen(["python3", file])
#             p.run()
#             multiprocessing.get_context('fork')
#             p = multiprocessing.Process(target=execute(file, windows))
#             p.run()


def execute(file, windows):pass
#     subprocess.run(["python3", file])
    # if not windows:
    #     os.system("chmod +x " + file)
    #     os.system("python3 " + file)
    # else:
    #     os.system("python " + file)


if __name__ == "__main__":
    main()
