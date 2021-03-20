import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

server=smtpmail.SMTP("youremail.com","your port number")


server.ehlo()

server.login("user-email","password")

'''incase you want to encript your password you should save it on diffferent text then you initialize it
with open("password.txt".r) as f:
    password=f.read()

'''
msg=MIMEMultipart()

msg['from']= 'john@gmail.com'
msg['to']='derik@gmail.com'
msg['subject']='just a testing mail'

with open('derik.txt','r') as f:
    message=f.read()

msg.attach(MIMEText(message,'plain'))

''' if you have an image then you can call it like this '''
filename='image.png'
attachment=open(filename,'rb')

'''then you call the payload in '''
p=MIMEBase('application','octet-stream')
p.set_payload(attachment.read())

'''encoders '''
encoders.encode_base64(p)
p.add_header('Content-Dispostion',f'attachment;filenam= {filename}')
msg.attach(p)
text=msg.as_string()
server.sendmail('mail@gmail.com','nnsjjd@gmail.com',text)