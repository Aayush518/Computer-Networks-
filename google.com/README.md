# TCP/IP Model: Accessing google.com

This README provides a detailed explanation of the processes involved in each layer of the TCP/IP model when you enter "google.com" in our web browser.

## Table of Contents
- [Application Layer](#application-layer)
- [Transport Layer](#transport-layer)
- [Internet Layer](#internet-layer)
- [Network Interface Layer](#network-interface-layer)

## Application Layer

The application layer is responsible for user interaction and data representation. Here's what happens:

1. **URL Parsing:**
   - The browser identifies the scheme (`http` or `https`), domain (`google.com`), path, query strings, and fragment identifiers.

2. **HSTS Check:**
   - Browser checks its preloaded HSTS list to see if it should enforce HTTPS.

3. **DNS Resolution:**
   - The browser checks its DNS cache.
   - If not found, it queries the OS's DNS cache.
   - If still not found, it queries the DNS resolver, eventually performing a recursive query if necessary.
   - The final result is an IP address for `google.com`.

4. **Protocol Selection:**
   - Based on the HSTS check and URL scheme, the browser selects HTTPS as the protocol.

5. **HTTP Request Preparation:**
   - The browser constructs an HTTP request (`GET / HTTP/2`), adds necessary headers (e.g., Host, User-Agent), and includes any relevant cookies.

## Transport Layer

The transport layer ensures reliable data transfer. Here's what happens:

1. **TCP Socket Creation:**
   - The browser creates a TCP socket using the IP address from the DNS resolution and port 443 (default for HTTPS).

2. **TCP Handshake:**
   - The browser initiates a three-way handshake:
     - SYN: The browser sends a SYN packet to the server.
     - SYN-ACK: The server responds with a SYN-ACK packet.
     - ACK: The browser sends an ACK packet, establishing the connection.

3. **TLS Handshake:**
   - The browser and server establish a secure connection:
     - Client Hello: The browser sends supported TLS versions, cipher suites, and compression methods.
     - Server Hello: The server responds with the selected TLS version, cipher suite, and its digital certificate.
     - Certificate Validation: The browser validates the server's certificate.
     - Key Exchange: The browser and server exchange keys to establish a secure session.
     - Finished Messages: Both parties send encrypted "Finished" messages to confirm the secure connection.

## Internet Layer

The internet layer handles logical addressing and routing. Here's what happens:

1. **Packet Creation:**
   - The browser's HTTP request is encapsulated in a TCP segment, which is then encapsulated in an IP packet.

2. **Routing:**
   - The packet is sent to the default gateway (usually the router).
   - The router examines the IP address and forwards the packet towards the destination (Google's server).
   - Routers along the path determine the best route for the packet until it reaches Google's server.

## Network Interface Layer

The network interface layer manages physical addressing and data transmission over the network. Here's what happens:

1. **Frame Creation:**
   - The IP packet is encapsulated in an Ethernet frame, which includes the MAC address of the destination.

2. **Data Transmission:**
   - The frame is sent over the physical network (e.g., Ethernet, Wi-Fi) to the next hop (e.g., router, switch).
   - Each device in the path forwards the frame to the next hop based on MAC addresses until it reaches the destination network.

3. **Frame Reception:**
   - The frame is received by Google's network interface.
   - The frame is decapsulated to retrieve the IP packet, which is then processed by Google's server.

## Conclusion

The process of accessing "google.com" involves multiple steps across the TCP/IP model layers. Each layer plays a crucial role in ensuring reliable and secure communication between your browser and Google's server. Understanding these layers helps in optimizing web applications and troubleshooting network issues.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
