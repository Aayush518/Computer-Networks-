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

### 1. Simulate Connecting Two Hosts on the Same Network Using Packet Tracer
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

### 2. Simulate Connecting Hosts on Different Networks Using Packet Tracer
- First add the 4 Laptops, 1 Router, 2 Switches to form network topology
- Connect devices
    - Connect Laptop0 and Laptop1 to Switch0
    - Connect Laptop2 and Laptop3 to Switch1
    - Connect Switch0 to Router (GigabitEthernet0/0)
    - Connect Switch1 to Router (GigabitEthernet0/1)
  
- Configure Laptop0 and Laptop1 to Switch0 and finally to router with IPv3 192.168.1.0. Assign IPs on the devices accordingly.
    - For laptop 0 (For example)
        - IP Address: 192.168.1.2
        - Subnet Mask: 255.255.255.0
        - Default Gateway: 192.168.1.1
- Configure Laptop2 and Laptop2 to Switch1 and finally to router with IPv3 11.12.1.0. Assign IPs on the devices accordingly.
- Enable Routing on Router
- Test the network
    - Open Command Prompt on Laptop0
    - Execute: ping 11.12.1.2
      
![different network](https://github.com/Aayush518/Computer-Networks-/assets/63596895/00eb1be3-5785-419c-b74e-74fb4277f81a)

### 3. Simulate System For Assigning IP Addresses Automatically To Host On Network Using DHCP
- First add the 4 Laptops, 1 Router, 2 Switches to form network topology
- Connect the Router to the Switch and Connect all End Devices to the Switches
- Add a DHCP server
    - Assign static IP Address to it
    - Specify the starting IP address and number of devices to facilitate
- Configure End Devices to Obtain IP Automatically
    - Click on each PC or Laptop
    - Go to the Desktop tab
    - Select IP Configuration
    - Choose DHCP
- Verify DHCP assignment
    - On each PC or Laptop, go to Command Prompt
    - Execute ipconfig
    - Verify that the IP address, subnet mask, and default gateway are correctly assigned.

<img width="867" alt="Screenshot 2024-07-12 at 12 42 04 AM" src="https://github.com/Aayush518/Computer-Networks-/assets/63596895/6de3e1b8-72d2-4ccb-8977-185aa170257d">

<img width="699" alt="Screenshot 2024-07-12 at 12 42 55 AM" src="https://github.com/Aayush518/Computer-Networks-/assets/63596895/c457297f-e7b3-4c4b-843e-e7255a1d9bb7">

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

