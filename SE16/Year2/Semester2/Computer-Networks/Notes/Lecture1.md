# Lecture 1

## Requirements of Internet Connection
- Physical Connection
- Logical Connection
- Application 

### Physical Connection

Network Interface Card (NIC)
- When selecting a NIC, consider the following factors:
    - Protocols:
        - Ethernet
        - Token Ring
        - FDDI
    - Types of Media:
        - Twisted-pair
        - Coaxial Wireless
        - Fiber-Optic
    - Types of System Bus
        - PCI
        - ISA

### Logical Connection (TCP/IP) description and configurtion

- Ethernet Address
    - 48 Bit number (the first 24 bits indicate the manufacturer, the
    last 24 bits are the unique number for each board/controller-chip
    assigned by the manufacturer)
    - AKA MAC-Address (Media Access Control
    Address)
    - Can be compared to Physical Address
- IP Address
    - 32 Bit number which represent to a logical connection
    - Can be compared to Mailing Address or Geological Address or
    Logical Address
    - Can be separated into 4 portions (8.8.8.8)
    - Can be changed depend on the location of your device
- NetMask
    - Network ID and Host ID
- DNS (Domain Name System)
    - Name version of the IP Address
- TCP/IP Transmission Control
    - Protocol/Internet Protocol us a set of protocol developed to allow
    computer to share resources


#### IP Config using DHCP

DHCP (Dynamic Host configurtion Protocol)
1. When the device is connected to the DHCP network, it will broadcast
to the MAC-Address of the network. If that network is not DHCP it will
ignore the broadcast (There is a special MAC-Address which is `FF:FF:FF`
which is used for broadcast in DHCP)
2. The DHCP response with the network information
    - NetMask
    - Default Gateway
    - Pool of IPs

#### Gateway and Router (Default Router)

Is used to send out data to the outside world.  
If send locally, just send it directly.  
- It has its own IP Address too.

#### Subner-Mask (NetMask)

- 32 Bit number, separated into 2 portions (All Network ID represent
by 1 and all Host Id represent by 0)
    - The first portion (24 bits) is Network ID
    - The second portion (8 bits) is Host ID

#### DNS (Domain Name Service)
- Just mapping of number to the IP to the name that human can remember.
- If the DNS got hacked, hacker can redirect the from the correct site
to their fake site to get your personal information.

#### Ping Command

Used to check whether the server is online or not.
- RTT (Round Trip Time)
- TTL (Time to Live)
- `127.0.0.1` reserved special IP Address for loop back, if you cannot
ping that it means you did not set up the physical connection correctly

##### How to know that you are capable to connect to the internet?

Answer:
1. Ping Physical Connection
```
ping 127.0.0.1
```
1. Ping Logical Connection
```
ping <DEFAULT_GATEWAY>
```
1. Ping Application
```
ping <SOME_DNS>
```

## Key Takeaway
- MAC-Address uses to map with the NIC
- IP Address uses to map with the location
- DNS uses to talk in the family.
- Gateway uses to talk with other people outside the family.
- We put ID and NetMask together to decide where to send the request
and response to.
- We mostly fixed the broadcast MAC-Address to `FF:FF:FF` because when
a new device joins into the network it can send the address of the DHCP
to the broadcaster (FF:FF:FF is the convention).
