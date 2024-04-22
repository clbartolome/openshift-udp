import socket

UDP_IP = "0.0.0.0"  # Listen on all available interfaces
UDP_PORT = 5000     # Change this to the port you're using

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print("UDP server listening on port", UDP_PORT)

while True:
    data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
    print("Received message:", data.decode())