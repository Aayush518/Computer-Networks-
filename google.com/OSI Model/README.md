# OSI Model: Accessing google.com

This README provides a detailed explanation of the processes involved in each layer of the OSI model when you enter "google.com" in your web browser.

## Table of Contents
- [Application Layer](#application-layer)
- [Presentation Layer](#presentation-layer)
- [Session Layer](#session-layer)
- [Transport Layer](#transport-layer)
- [Network Layer](#network-layer)
- [Data Link Layer](#data-link-layer)
- [Physical Layer](#physical-layer)
- [Conclusion](#conclusion)

## Application Layer

The application layer is responsible for user interaction and high-level protocols. Here's what happens:

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

## Presentation Layer

The presentation layer handles data formatting, encryption, and compression. Here's what happens:

1. **Data Formatting:**
   - The HTTP request is formatted according to HTTP/2 specifications.

2. **Encryption:**
   - If using HTTPS, the data is prepared for encryption (actual encryption occurs in the session layer).

3. **Compression:**
   - Any compression algorithms specified in the HTTP headers are applied.

## Session Layer

The session layer manages sessions between applications. Here's what happens:

1. **Session Establishment:**
   - For HTTPS, the TLS handshake process begins:
     - Client Hello: The browser sends supported TLS versions, cipher suites, and compression methods.
     - Server Hello: The server responds with the selected TLS version, cipher suite, and its digital certificate.

2. **Session Management:**
   - Keeps track of the communication session between the browser and the server.

3. **Authentication:**
   - The browser validates the server's certificate as part of the TLS handshake.

## Transport Layer

The transport layer ensures reliable data transfer. Here's what happens:

1. **TCP Socket Creation:**
   - The browser creates a TCP socket using the IP address from the DNS resolution and port 443 (default for HTTPS).

2. **TCP Handshake:**
   - The browser initiates a three-way handshake:
     - SYN: The browser sends a SYN packet to the server.
     - SYN-ACK: The server responds with a SYN-ACK packet.
     - ACK: The browser sends an ACK packet, establishing the connection.

3. **Segmentation:**
   - The data from upper layers is divided into segments.

4. **Flow Control:**
   - Mechanisms like sliding window are used to manage data flow between sender and receiver.

## Network Layer

The network layer handles logical addressing and routing. Here's what happens:

1. **Packet Creation:**
   - The TCP segments are encapsulated in IP packets.

2. **Routing:**
   - The packet is sent to the default gateway (usually the router).
   - The router examines the IP address and forwards the packet towards the destination (Google's server).
   - Routers along the path determine the best route for the packet until it reaches Google's server.

## Data Link Layer

The data link layer manages physical addressing and error detection. Here's what happens:

1. **Frame Creation:**
   - The IP packet is encapsulated in a frame (e.g., Ethernet frame), which includes the MAC address of the destination.

2. **Error Detection:**
   - Adds error-checking information (e.g., CRC) to the frame.

3. **Media Access Control:**
   - Manages access to the physical medium (e.g., CSMA/CD for Ethernet).

## Physical Layer

The physical layer handles the actual transmission of raw bits over the physical medium. Here's what happens:

1. **Signal Encoding:**
   - The bits from the data link layer are converted into appropriate signals for the physical medium (e.g., electrical signals for Ethernet, radio waves for Wi-Fi).

2. **Data Transmission:**
   - The signals are transmitted over the physical medium.

3. **Physical Connectivity:**
   - Manages the physical connections and interfaces (e.g., Ethernet ports, Wi-Fi antennas).

## Conclusion

The process of accessing "google.com" involves multiple steps across all seven layers of the OSI model. Each layer plays a crucial role in ensuring reliable, secure, and efficient communication between your browser and Google's server. Understanding these layers helps in designing robust network applications, troubleshooting issues, and optimizing network performance.

