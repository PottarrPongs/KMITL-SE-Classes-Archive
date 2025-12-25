# Lecture 2

## Line Configuration

### Point to Point Configuration 

From a point to another point.

### Multipoint Configuration

Need a rule to enforce to prevent collision.

## Network Topology

### Topology for Wired Connection

#### Mesh Topology

Point to Point to everyone
- Connect directly without middle server
- Almost impossible to implement IRL
- Good for small network
- ZigBee (6B) Protocol
    - 2.4 GHz.
    - Communicate within network and trying to create Mesh Topology

#### Star Topology

Connect everyone to a `Switch` or a `Hub` to centralize network
- You need a center node.

#### Tree Topology (Extended Star Topology)

Can be referenced as Hierarchical or Cascading tar or Extended Star.

#### Bus Topology

More like System bus in CAO class, there can be only one sender at a
time, the listener can ignore the media to save computing power.

E.g.:  
- Access point for the wireless internet

#### Ring Topology

Cycle in circle like ring
- Forward from to another
- Basket Ring Topology
    - There is a token.
    - Every node has a basket
    - When a token is forward to that basket, they have right to send
    data.
    - If they currently do not have basket, they have no right to send
    data, only receive.

### Topology for Wireless Connection

- Wireless LAN

> [!NOTE]  
> Standard Ethernet in IEEE: IEEE802.3  
> Standard Wireless in IEEE: IEEE802.11

### Transmission Mode

#### Simplex Mode

One way Communication  

E.g.:  
- TV broadcast
- Radio broadcast

#### Half-Duplex

A device cam be one of the state at a time and the state is changeable.
- Sender
- Receiver

E.g.:  
- Walkie Talkie

#### Full-Duplex

A device can be in both state at the same time (Sender and Receiver at
the same time).

### Categories of Networks

- Local Area Network (LAN) $\rightarrow$ 0m - 10 KM (Room, Building Campus)
- Local Area Network (LAN) $\rightarrow$ 10 KM - 100 KM (City)
- Local Area Network (LAN) $\rightarrow$ 100 KM - 10000 KM (Country Continent)
- Internet $\rightarrow$ 10000 KM++ (Planet)

No need to remember the length of the network.

### Connection-Oriented an Connectionless Service

#### Connection-Oriented Service

Send and wait till it arrives at the destination and can talk in the
same time.

Purposes:
- Reliability of connection (correctness of the data)

Drawback:
- Speed

How?:
1. Establish a connection
2. Use the connection (Send data)
3. Release the connection (Close the connection)


#### Connectionless Service

Send and hope it arrives at the destination without knowing anything.

Purposes:
- Same model like the Postal office.

Drawback:
- Some Packet lost
- Lower quality

### Protocol Hierarchy

> [!NOTE]  
> Protocol is the set of the language which both side should use to
communicate correctly.

#### Protocol Layers

Can be many variety of layers depend on any Protocol.

### Reference Models

##### Layers of IEEE OSI

- Physical Layer (P.)
    - Responsibility: Line Configuration (Bit Transmission)
    - Data Transmission Mode
        - Simplex
        - Half-Duplex
        - Full-Duplex
    - Signal
        - Which frequency
        - Which method of signaling
        - Packet
        - Logical Address (IP Address)
    - Encoding
        - Binary Encoding (1, 0)
        - Manchester Encoding (1 = 10, 0 = 01 (NOT DETECTING EDGES)
            - Why?
                - Answer: To discharge the wired not to get false
                signal from long discharging time.
    - Interface
        - How are we going to connect them?
            - Fiber Optic
            - LAN Line
    - Medium (Media)
        - Copper Line (For sending electron for electricity)
        - Fiber Optic (Sending signal via light)
        - Last one will be talked again later...
- Data Link Layer (D.)
    - Responsibility: Node-to-node Delivery
    - Addressing
        - Physical Address (MAC Address)
    - Access Control
        - Mechanism for any device to take control of the media.
    - Flow Control
        - Mechanism to control the speed of both sender and receiver
        not to lost frames. (Get the most frames that can both work
        on both sides.)
    - Error Control
        - Error Detection
            - Throw the error to the bin and ask sender to send again.
        - Error Collection
            - Collect the error messages but need more data in the
            message.
            - Lose speed and take more data in each transmission.
    - Synchronization
        - $\Delta t$ (Time difference between each signal)
        - Preamble Bit: First 56 Bits will define this to use to
        calculate $\Delta t$.
    - Frame: The data which is sent in this layer is called `Frame`.
    - Sub-Layers:
        - LLC
        - MAC
- Network Layer (N.)
    - Responsibility: Source-to-destination Delivery (Best Effort)
    - Logical Addressing
        - IP Address
    - Routing
        - Routing Algorithm
            - Dijkstra Algorithm
            - Another one will be talked about later...
    - Address Transformation (Logical $\iff$ Physical)
        - Protocol
            - Address Resolution Protocol (ARP): For mapping IP Address
            to MAC Address.
    - Multiplex
        - Opening many browser tabs using only 1 IP Address (Process
        managing).
    - Packet: The data which is sent in this layer is called `Packet`.
- Transport Layer (T.)
    - Responsibility: End-to-end message Delivery Control
    (Process-to-process Delivery Control)
    - Service-point (Port) Addressing
        - Used to map connection to your process ID
        - TCP, UDP, ICMP
    - Establish, maintain, terminate virtual circuit
- Session Layer (S.)
    - Responsibility: Session Management (Form and session huge data)
    (Programmer's job)
    - Dialog controller, it establishes, maintains and synchronizes the
    interaction between application
         - Sync between applications
- Presentation Layer (P.)
    - Responsibility: Translation (Programmer's job)
    - Format Data
    - Data Structure
    - Encryption, compression and security
- Application Layer (A.)
    - Responsibility: Application (e.g.: mail, web, etc.) (Programmer's
    job)

`Please Do Not Trust Sam's Pet Aligator.`  
`Australian Post Send To Nowhere Doesn't Present`

> [!IMPORTANT]  
> This class mainly focus on Data Link, Network and Transport Layers


### Network Devices

#### Repeater

- Run on Physical Layer
- The longer the line, the weaker the signal is going to be. We use the
repeater to maintain the signal strength.

> [!NOTE]  
> LAN is for shorter than 100 m.  
> Fiber Optic is for a long intercontinental communication.

#### HUB (Obsoleted)

- Run on Physical Layer
- When data is sent to the HUB, it will applify and send to every other
node. But slow because it works the same way as the Bus
- Types:
    - Passive
    - Active

#### Switch

- Run on Data Link Layer
- How it work?
    - Once initially send for the first time to the switch, it record
    a new port and next time will send to the correct MAC Address.
    - It sends to the specific port with the specific MAC Address.

#### Bridge

- Run on Physical Layer and Data Link Layer MAC Sub-Layer
- Used to join two network together. (Obsoleted)
- Used to convert between Ethernet and Internet Frame format
(Current day commercial name: Access Point)

#### Router

- Run on ...
- Used to segment a large network
- Can also used to connect LAN to WAN

### ITU

#### Main Sectors

#### Classes of Members



## Key Takeaway

- We mostly talk about IEEE802.3 in this class.
- Back in old days, we send data bit by bit, so now we still use
bit/second but in storage, we store in size of byte.

## Midterm Leak

- Recognize which device is in which Transmission Mode

