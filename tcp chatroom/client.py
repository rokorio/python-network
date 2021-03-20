import socket
import threading

nickname=input("choose yotu nickname:::::")

cilent=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clint.connect(('127.0.0.1',20000))

def receive():
    while True:
        try:
            message=client.recv(1024).encode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print("An error occurred")

def write():
    while True:
        message=f'{nickname}:{input()}'
        cilent.send(message.encode())


receive_thread=threading.Thread(target=receive)
receive_thread.start()

write_thread=threading.Thread(target=write)
write_thread.start()

