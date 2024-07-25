# 🌐 Computer Networks 

# 🌪️ BitTorrent Project Hub

Welcome to the central hub for our BitTorrent implementation projects! Here you'll find links to both our successful implementation and our experimental attempts.

## 🚀 Successful Implementation

### [TClient: The Didactic Parakeet](https://github.com/Aayush518/TClient-didactic-parakeet)


🎉 **Fully Functional BitTorrent Client**

- ✅ Complete peer-to-peer file sharing
- 🔒 efficient downloads
- 🖥️ User-friendly interface

> "TClient: Where efficiency meets simplicity in the world of torrents!"

[👉 Explore TClient](https://github.com/Aayush518/TClient-didactic-parakeet)


## 🧪 Experimental Implementations

### [BitTorrent Implementations Lab](https://github.com/Aayush518/BitTorrent-Implementations)

🔬 **A Collection of BitTorrent Experiments**

- 🚧 Work-in-progress implementations
- 🌱 Learning ground for BitTorrent protocols

> "Where failures are just stepping stones to success!"

[🔍 Dive into the Lab](https://github.com/Aayush518/BitTorrent-Implementations)


## 📊 Project Comparison

| Feature | TClient | BitTorrent Lab |
|---------|---------|----------------|
| Status  | ✅ Complete | 🚧 In Progress |
| Functionality | 🌟 Proper | 🔬 Partial |
| Purpose | 🚀 Self-Use| 🧠 Learning |



> 🔗 Connecting peers, one torrent at a time!


<sub>🔒 Remember to use BitTorrent responsibly and respect copyright laws.</sub>

# 🌐 A Day in the Life of a Web Request

💡 **Note:** This provides a simplified level overview. For more detailed information on each step, see [WebRequestActions](https://github.com/Aayush518/Computer-Networks-/blob/main/WhatHappensWhenYouEnterGoogleDotComAndHitEnter.pdf).

## 🚀 Introduction

A detailed steps involved in making a web request from a hostel room to www.google.com, integrating knowledge from various layers of the network protocol stack.

## 🔌 Connecting to the Network

Upon connecting a laptop to the hostel's campus network, the device must obtain an IP address using the Dynamic Host Configuration Protocol (DHCP):

1. 📡 **DHCP Discover:** The laptop sends a DHCP Discover message to find available DHCP servers.
2. 📬 **DHCP Offer:** A DHCP server responds with a DHCP Offer message, providing an IP address and other network configurations.
3. 📝 **DHCP Request:** The laptop sends a DHCP Request message to request the offered IP address.
4. ✅ **DHCP Acknowledgment:** The DHCP server acknowledges with a DHCP ACK message, confirming the lease of the IP address.

> After this exchange, the laptop has an IP address, the addresses of DNS servers, and the gateway router.

## 🔍 DNS Request

To access www.google.com, the laptop needs to resolve the domain name to an IP address using the Domain Name System (DNS):

1. 🔎 **DNS Query:** The DNS request is prepared and encapsulated.
2. 🤝 **ARP Request:** If needed, the laptop sends an ARP request for the gateway router's MAC address.
3. 🚀 **Forwarding DNS Query:** The laptop sends the DNS query to the gateway router.
4. 🧩 **DNS Resolution:** The DNS server resolves the domain name and returns the IP address.

## 🌐 HTTP Request

With the resolved IP address, the laptop can now make an HTTP request:

1. 🤝 **TCP Connection:** A TCP connection is established using a three-way handshake:
   - 👋 **SYN:** Laptop sends SYN packet
   - 👍 **SYN-ACK:** Server responds
   - ✅ **ACK:** Laptop acknowledges
2. 📤 **HTTP GET Request:** The laptop sends an HTTP GET request for the Google homepage.
3. 📥 **Server Response:** The Google server sends back the requested web page.
4. 🎨 **Rendering the Web Page:** The browser receives the HTML, parses it, and requests additional resources.

## 📦 Encapsulation and Decapsulation

Each step involves encapsulation and decapsulation through the network layers:

| Layer | Function |
|-------|----------|
| 📱 Application | HTTP request and response |
| 🚢 Transport | TCP ensures reliable delivery |
| 🌐 Network | IP addresses for routing |
| 🔗 Link | Ethernet frames for local transmission |
| 💻 Physical | Actual transmission of bits |

The process of loading a web page involves multiple network layers and protocols working together seamlessly. From obtaining an IP address via DHCP, resolving domain names via DNS, establishing a TCP connection, to making an HTTP request, each step ensures reliable communication across the network. This comprehensive journey highlights the complexity and efficiency of modern networking.


## 📚 Assignments

### 📘 Assignment 1: IP Addressing and Subnetting

**Description:** Explored IP addressing, subnetting, and network configurations using `ifconfig` and Packet Tracer.

#### 🔑 Key Concepts:
- Subnet masks and binary representation
- Usable IP address calculation
- Packet Tracer network simulations

#### 📊 Sample Configuration:
- **IP Address:** 192.168.1.2
- **Subnet Mask:** 255.255.255.0 (0xffffff00 in hex)

#### 🛠️ Practical Simulations:

1. **Connecting Two Hosts on the Same Network**
   - Used Cisco Packet Tracer
   - Connected PC and Laptop with Copper Straight-Through cable
   - Configured IP addresses (e.g., 192.168.1.2 and 192.168.1.3)
   - Tested connectivity using `ping`

   ![Same Network Simulation](https://github.com/Aayush518/Computer-Networks-/assets/63596895/dae1a561-59fa-438c-bfce-a57ee41ba345)

2. **Connecting Hosts on Different Networks**
   - Created topology with 4 Laptops, 1 Router, 2 Switches
   - Configured two subnets: 192.168.1.0 and 11.12.1.0
   - Enabled routing on the router
   - Tested inter-network connectivity

   ![Different Networks Simulation](https://github.com/Aayush518/Computer-Networks-/assets/63596895/00eb1be3-5785-419c-b74e-74fb4277f81a)

3. **DHCP Configuration**
   - Set up DHCP server with static IP
   - Configured end devices to obtain IP automatically
   - Verified DHCP assignment using `ipconfig`

   ![DHCP Configuration](https://github.com/Aayush518/Computer-Networks-/assets/63596895/c457297f-e7b3-4c4b-843e-e7255a1d9bb7)

#### 📁 Resources:
- [CN_ASSIGNMENT_I.pdf](Assignments/CN_ASSIGNMENT_I.pdf)

### 📗 Assignment 2: Introduction to Computer Networks

**Description:** Covered fundamental concepts including OSI model and TCP/IP comparisons.

#### 🔑 Key Topics:
- Definition of Computer Networks (CN)
- OSI model layers and functions
- OSI vs TCP/IP model comparison

#### 📁 Resources:
- [CN_Assignment_2.pdf](CN_Assignment_2.pdf)



#### 📁 Resources:
- [Flow-of-Web.pdf](Flow-of-Web.pdf)

## 🧠 LeetCode Solutions

### 🌐 Network Algorithms

#### 🛫 Cheapest Flight Within K Stops
- Solution approach and code available in PDF

### 🕸️ Graph Algorithms

#### ⏱️ Network Delay Time
- Solution approach and code available in PDF


---

💡 **Note:** This README will be updated as the course progresses and new assignments are completed.
