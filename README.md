# Computer-Communication-Networking
To run the TCP and UDP flies:

TCP:
First start the python tcp_server.py file in dedicated terminal. Run the tcp_client.py file in a separate dedicated terminal. Then you can observe the packets transferred.
UDP:
First start the UDP server: python udp_server.py. Then run the python udp_client.py file in a separate dedicated terminal. 


Expected Output:

TCP:
Server logs received messages and calculates average latency and throughput. Client sends 100 messages, logs round-trip times, and displays average latency and throughput.

UDP:
Server logs received messages, simulates packet loss, and calculates packet loss rate. Client sends 100 messages, logs round-trip times, and displays average latency, packet loss rate, and throughput. 


Compare the average round-trip time (RTT) for TCP and UDP.

TCP has higher average RTT due to connection setup (3-way handshake), acknowledgment mechanisms, and due to retransmission of lost packets. It is also evident from the screen shot above. UDP has Lower average RTT because it is connectionless, does not wait for or give acknowledgments, and does not retransmit lost packets. It also has less protocol overhead.

Why Does UDP Have Lower Latency Than TCP?

UDP does not require a 3-way handshake like TCP. UDP does not wait for ACKs, reducing waiting time. Also, UDP does not retransmit lost packets, avoiding additional delays. Furthermore, there is less overhead as UDP has a smaller header and no flow control or congestion control mechanisms.

What happens when some UDP packets are lost? 

Lost packets are dropped and not retransmitted. Data will be missing, but communication continues without delay and in most cases the lost data doesn’t affect the application that much.

Why does TCP ensure that all packets arrive correctly?

TCP uses acknowledgments (ACKs) and retransmissions to ensure that the packets arrive correctly. If a packet is lost, TCP detects it through missing ACKs and retransmits the packet. This retransmission is done to ensure reliable delivery of all packets, ensuring no data is lost.

Which protocol is faster for bulk data transfer?

UDP is faster for bulk data transfer because it has no overhead for acknowledgments, retransmissions, or connection management. 
Why does TCP introduce overhead due to acknowledgments?
TCP requires acknowledgments (ACKs) for every packet to ensure reliable delivery. TCP introduces overhead due to acknowledgments, retransmissions, and connection management, reducing throughput.

When should an application use TCP instead of UDP?

An application should use TCP when reliability is important so that data must be delivered completely and correctly (e.g., file transfers, web browsing). It is also used when data must arrive in the same order it was sent (e.g., email, database transactions). TCP also ensures that the sender and receiver manage data flow to avoid overwhelming either side. TCP is also used when retransmission of lost or corrupted packets is required.

Real-world examples (e.g., HTTP, VoIP, video streaming).

•	HTTP/HTTPS (Web Browsing) uses TCP to ensure web pages and resources are loaded completely and correctly like loading a website: Google or YouTube.

•	Email (SMTP, IMAP, POP3) uses TCP to ensure emails are delivered reliably and in the correct order. Example: Sending an email via Gmail or Outlook.

•	File Transfer (FTP, SFTP) uses TCP to ensure files are transferred without errors or missing data. For instance: uploading a file to Google Drive or downloading from a server.

•	VoIP (Voice over IP): Uses UDP for real-time voice communication with low latency. Example: Skype, Zoom, or WhatsApp calls.

•	Online Gaming: uses UDP for real-time gameplay with minimal delay. Example: Fortnite, Call of Duty, or League of Legends. 

•	DNS (Domain Name System) uses UDP for fast resolution of domain names to IP addresses. For example: looking up google.com to get its IP address. 

•	Live Broadcasting uses UDP for transmitting live audio/video feeds with low latency. For example: Live sports broadcasts or news streaming.




To accomplish this task, I referred to online resources like tutorials on real-world use cases for TCP and UDP. I also used the Top down approach book to build the basic understanding of socket programming.
