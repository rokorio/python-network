'''portscanner is script to scan open ports in serveror any other computer devices '''
import threading 
import queue
import socket

target='10.3.2.55'
open_ports=[]

def scanport(port):
    try:
        sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.connect((target,port))
        return True
    except:
        return false

# for port in range(1,1024):
#     result=scanport(port)
#     if result:
#         print('for port {} is open '.format(port))
#     else:
#         print('port {} is closed'.format(port))

def fill_port(port_list):
    for port in port_list:
        queue.put(port)

def worker():
    while not queue.Empty():
        port=queue.GET(port)
        if scanport(port):
            print("port {} is open".format(port))
            open_ports.append(port)


port_list=range(1,1024)
fill_port(port_list)

thread_list=[]

for t in range(10):
    thread=threading.Thread(target=worker)
    thread_list.append(thread)

for thread in thread_list:
    thread.start()

for thread in thread_list:
    thread.join()

print("open ports {}".format(open_ports))