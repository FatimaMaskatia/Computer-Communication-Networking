import socket
import time

HOST = '127.0.0.1'  
PORT = 12345  

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
# 100 messages to be sent to the server
messages = 100

def send_messages():
    total_latency = 0
    for i in range(messages):      
        message = f"message {i + 1}"
        send_time = time.time()

        client.send(f"{message}|{send_time}".encode('utf-8'))

        response = client.recv(1024).decode('utf-8')
        receive_time = time.time()

        latency = receive_time - send_time
        total_latency = total_latency  + latency

        print(f"sent: {message} | received: {response} | latency: {latency:.6f} seconds")

    average_latency = total_latency / messages
    if total_latency > 0:
        throughput = messages / total_latency
    else:
        throughput = 0
    print(f"\naverage latency is {average_latency:.6f} seconds")
    print(f"throughput is {throughput:.2f} messages per second")

send_messages()
client.close()
