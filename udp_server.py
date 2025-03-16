import socket
import random
import time

HOST = '127.0.0.1'  
PORT = 12346        

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((HOST, PORT))
print(f"UDP Server listening on {HOST} -> {PORT}...")

PACKET_LOSS_RATE = 0.2

def packets():
    total_messages = 0
    total_received = 0

    while True:        
        data, client_address = server_socket.recvfrom(1024)
        total_messages = total_messages + 1

        if random.random() < PACKET_LOSS_RATE:
            print(f"Packet lost (simulated): {data.decode('utf-8')}")
            continue

        message, send_time = data.decode('utf-8').split('|')
        send_time = float(send_time)

        receive_time = time.time()

        latency = receive_time - send_time

        response = f"Received: {message}"
        server_socket.sendto(response.encode('utf-8'), client_address)

        total_received += 1
        print(f"Received: {message} | Latency: {latency:.6f} seconds")

        if total_received >= 100:
            break

    packet_loss_rate = (total_messages - total_received) / total_messages
    print(f"\nPacket Loss Rate: {packet_loss_rate * 100:.2f}%")

packets()

server_socket.close()
