import socket
import time

HOST = '127.0.0.1'  
PORT = 12346        

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

NUM_MESSAGES = 100

def send_messages():
    total_latency = 0
    total_sent = 0
    total_received = 0

    for i in range(NUM_MESSAGES):
       
        message = f"Message {i + 1}"
        send_time = time.time()

        client_socket.sendto(f"{message}|{send_time}".encode('utf-8'), (HOST, PORT))
        total_sent += 1

        client_socket.settimeout(1) 
        try:
            response, _ = client_socket.recvfrom(1024)
            receive_time = time.time()

            latency = receive_time - send_time
            total_latency = total_latency + latency
            total_received = total_received + 1

            print(f"Sent: {message} | Received: {response.decode('utf-8')} | Latency: {latency:.6f} seconds")
        except socket.timeout:
            print(f"Sent: {message} | Packet lost (no response)")

    if total_received > 0:
        avg_latency = total_latency / total_received
        packet_loss_rate = (total_sent - total_received) / total_sent
        throughput = total_received / (time.time() - start_time)
    else:
        avg_latency = 0
        packet_loss_rate = 1.0
        throughput = 0

    print(f"\nAverage Latency: {avg_latency:.6f} seconds")
    print(f"Packet Loss Rate: {packet_loss_rate * 100:.2f}%")
    print(f"Throughput: {throughput:.2f} messages per second")

start_time = time.time()
send_messages()

client_socket.close()
