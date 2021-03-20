import threading
import socket


host='127.0.0.1'
port= 20000

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))

clients=[]
nicknames=[]

def broadcast(message):
    for client in clients:
        client.send(message)


def handleclient(client):
    while True:
        try:
            message=client.recv(1024)
            broadcast(message)
        except:
            index=clients.index(client)
            clients.remove(client)
            nickname=nicknames[index]
            broadcast(f"{nickname} has left" .encode('ascii'))
            nicknames.remove(nickname)
            break



def receive():
    while True:
        client ,address=server.accept()
        print(f"connected with {str(address)}")

        client.send('NICK'.encode('ascii'))
        nickname=client.recv(1024).decode('ascii')

        clients.append(client)
        nicknames.append(nickname)
        print(f'nickname of the client is{nickname}')

        broadcast(f'{nickname} is connected'.encode('ascii'))

        client.send(f'connected to the server'.encode('ascii'))

        thread=threading.Thread(target=handleclient,args=(client,))
        thread.start()
receive()