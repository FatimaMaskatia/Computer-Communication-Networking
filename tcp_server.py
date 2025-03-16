import socket
import time
# using the local host address to test the TCP server and client
HOST = '127.0.0.1' 
PORT = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)
print(f"TCP server waiting for connection {HOST} -> {PORT}...")

client_socket, client_address = server.accept()
print(f"connected to client: {client_address}")

def client():
    total_messages = 0
    total_latency = 0

    while True:        
        data = client_socket.recv(1024).decode('utf-8')
        if not data:
            break

        receive_time = time.time()

        message, send_time = data.split('|')
        send_time = float(send_time)

        latency = receive_time - send_time
        total_latency = total_latency + latency
        total_messages = total_messages + 1

        response = f"received: {message}"
        client_socket.send(response.encode('utf-8'))

        print(f"received: {message} | latency: {latency:.6f} seconds")

    if total_messages > 0:
        average_latency = total_latency / total_messages
        if total_latency > 0:
            throughput = total_messages / total_latency
        else:
            throughput = 0 
        print(f"\naverage latency is {average_latency:.6f} seconds")
        print(f"throughput is {throughput:.2f} messages per second")

    client_socket.close()
    server.close()

client()
