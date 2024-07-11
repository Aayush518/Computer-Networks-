# Computer Networks Semester Assignments Overview

## Assignment 1: IP Addressing and Subnetting

**Description:** Assignment 1 focused on understanding IP addressing, subnetting, and network configurations using command like `ifconfig` and tool like Packet Tracer.

- **IP Address:** 192.168.1.2
- **Subnet Mask:** 255.255.255.0 (0xffffff00 in hexadecimal)

### Key Concepts Covered:
- Explanation of subnet masks and their binary representation.
- Calculation of usable IP addresses in a subnet (28 - 2 = 254).
- Packet Tracer simulation demonstrating network configurations.

### Resources:
- [CN_ASSIGNMENT_I.pdf](CN_ASSIGNMENT_I.pdf): Theoretical overview and Packet Tracer simulation.



## Assignment: Simulate Network Connection Using Packet Tracker

### Prerequisites
- Cisco Packet Tracer installed on your computer. You can download it from Cisco's official website.
- Basic understanding of networking concepts.

### 1. Simulating Connecting Two Hosts on the Same Network Using Packet Tracer
### Steps to reproduce
- Open Cisco Packet Tracer
- Create a new network by selecting File > New from the menu.
- From the device type selection box at the bottom, choose End Devices.
- Drag and drop one PC and one Laptop devices onto the workspace.
- Establish connection between them using a 'Copper Straight-Through' cable.
- Click on laptop
    - Go to the Desktop tab and select IP Configuration.
    - Set the IP Address to 192.168.1.2 and the Subnet Mask to 255.255.255.0.
- Repeat above step for PC, but this time set IP Address to 192.168.1.3
- To test the connectivity
    - Click on PC0.
    - Go to the Desktop tab and select Command Prompt.
    - Type ping 192.168.1.3 and press Enter.

![ScreenRecording2024-07-11at11 24 22PM-ezgif com-video-to-gif-converter](https://github.com/Aayush518/Computer-Networks-/assets/63596895/dae1a561-59fa-438c-bfce-a57ee41ba345)
<img width="303" alt="Screenshot 2024-07-11 at 11 55 01 PM" src="https://github.com/Aayush518/Computer-Networks-/assets/63596895/77d4c502-1a9d-4584-bfb0-073341831b99">


## Assignment 2: Introduction to Computer Networks

**Description:** Assignment 2 covered fundamental concepts in computer networks, including the OSI model, differences between OSI and TCP/IP models.

### Key Topics:
- What is Computer Networks (CN)?
- OSI model layers and their functions.
- Comparison between OSI and TCP/IP models.

### Resources:
- [CN_Assignment_2.pdf](CN_Assignment_2.pdf): Detailed explanation and diagrams.

## Ongoing Assignment: Flow of Web Traffic

**Description:** This assignment evolves throughout the semester, aiming to provide an in-depth understanding of the flow of web traffic. It will be updated periodically as new concepts are learned.

### Current Topics Explored:
- Basics of HTTP/HTTPS protocols.
- Client-server communication.
- DNS resolution process.
- TCP handshake process.
- Web server types and configurations.

### Resources:
- [Flow-of-Web.pdf](Flow-of-Web.pdf): Current overview and updates.

## Leetcode Solutions

### Network Algorithms

#### Cheapest Flight Within K Stops

**Description:** This PDF document contains a solution approach and code for the Leetcode problem "Cheapest Flight Within K Stops".

### Graph Algorithms

#### Network Delay Time

**Description:** This PDF document contains a solution approach and code for the Leetcode problem "Network Delay Time".

