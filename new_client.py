import socket
import time

c= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while True:
    your_message = input('Enter your message: ')
    new_message = your_message.encode('ascii')
    c.sendto(new_message,('192.168.0.121',19358))
    print("data send..")
    # recieve
    time.sleep(1)
    print(c.recv(1024).decode())
c.close()