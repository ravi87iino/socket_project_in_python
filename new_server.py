import socket
import time

s= socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #nothing between mean it will take default (ipv4 , udp)
s.bind(('192.168.0.121',19358))
print('binding done')

while True:
    data = s.recv(1024).decode()
    time.sleep(1)
    print(data)
    #reply of data
    reply = input("enter your response: ")
    new_rep = reply.encode('ascii')
    s.sendto(new_rep,data[1])
s.close()