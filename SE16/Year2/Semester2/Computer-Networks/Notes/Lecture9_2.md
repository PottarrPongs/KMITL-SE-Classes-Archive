# Lecture 9.2

## Classes of TCP/IP Addresses

| Class |     |     |     |     |     |     |     |     |
| :---: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| A | 0 | * | * | * | * | * | * | * |
| B | 1 | 0 | * | * | * | * | * | * |
| C | 1 | 1 | 0 | * | * | * | * | * |
| D | 1 | 1 | 1 | 0 | * | * | * | * |
| E | 1 | 1 | 1 | 1 | 0 | * | * | * |

> [!NOTE]  
> `Class D` is reserved to multicast network.  
> `Class E` is reserved for research.

## Network/Host portion for each class

- Class A: `N.H.H.H`
- Class B: `N.N.H.H`
- Class C: `N.H.H.H`
- Class D
- Class E

## List of Private Natwork IP

- `10.0.0.0/8`
- `172.160.0.0/12`
- `192.168.0.0/16`

Else are public IP.

> [!NOTE]  
> `0.0.0.0/8` is reserved.  
> `127.0.0.0/8` is reserved for `loopback`.  
> `128.0.0.0/16`, `191.0.0.0/16` and `192.0.0.0/24` are once reserved
> but now being used by internet providers.



## Appendix

### EX1

Question:

`199.1.1.0/24`

Department Portions

- D1: 20
- D2: 20
- D3: 40
- D4: 40
- D5: 20
- D6: 20

Solution:

Department Portions

- D1: 20 $\rightarrow$ 32
- D2: 20 $\rightarrow$ 32
- D3: 40 $\rightarrow$ 64
- D4: 40 $\rightarrow$ 64
- D5: 20 $\rightarrow$ 32
- D6: 20 $\rightarrow$ 32

We divide 0..255 into 4 portions:
- `0..63`
- `64..127`
- `128..191`
- `192..255`

Then we split `0..63` and `64..127` in half.
- `0..31` $\rightarrow$ D1
- `32.63` $\rightarrow$ D2
- `64..95` $\rightarrow$ D5
- `96..127` $\rightarrow$ D6
- `128..191` $\rightarrow$ D3
- `192..255` $\rightarrow$ D4

Assign them into portions:

#### Portion 1

`199.1.1.0/26`

- Net ID: `199.1.1.0`
- Broadcast: `199.1.1.63`
- Netmask: `255.255.255.192`


#### Portion 2

`199.1.1.64/26`

- Net ID: `199.1.1.64`
- Broadcast: `199.1.1.127`
- Netmask: `255.255.255.192`

#### Portion 3

`199.1.1.128/26`

- Net ID: `199.1.1.128`
- Broadcast: `199.1.1.191`
- Netmask: `255.255.255.192`

#### Portion 4

`199.1.1.192/26`

- Net ID: `199.1.1.192`
- Broadcast: `199.1.1.255`
- Netmask: `255.255.255.192`

Then, we portions `Portion 1` and `Portion 2` in half:

#### Portion 1.1

`199.1.1.0/27`

- Net ID: `199.1.1.0`
- Broadcast: `199.1.1.31`
- Netmask: `255.255.255.224`

#### Portion 1.2

`199.1.1.32/27`

- Net ID: `199.1.1.32`
- Broadcast: `199.1.1.63`
- Netmask: `255.255.255.224`

#### Portion 2.1

`199.1.1.64/27`

- Net ID: `199.1.1.64`
- Broadcast: `199.1.1.95`
- Netmask: `255.255.255.224`

#### Portion 2.2

`199.1.1.96/27`

- Net ID: `199.1.1.96`
- Broadcast: `199.1.1.127`
- Netmask: `255.255.255.224`

Then we assign to the departments:

- D1: `199.1.1.0/27`
    - Net ID: `199.1.1.0`
    - Broadcast: `199.1.1.31`
    - Netmask: `255.255.255.224`
    - Default Gateway: `199.1.1.1`
- D2: `199.1.1.32/27`
    - Net ID: `199.1.1.32`
    - Broadcast: `199.1.1.63`
    - Netmask: `255.255.255.224`
    - Default Gateway: `199.1.1.33`
- D3: `199.1.1.128/26`
    - Net ID: `199.1.1.128`
    - Broadcast: `199.1.1.191`
    - Netmask: `255.255.255.192`
    - Default Gateway: `199.1.1.129`
- D4: `199.1.1.192/26`
    - Net ID: `199.1.1.192`
    - Broadcast: `199.1.1.255`
    - Netmask: `255.255.255.192`
    - Default Gateway: `199.1.1.193`
- D5: `199.1.1.64/27`
    - Net ID: `199.1.1.64`
    - Broadcast: `199.1.1.95`
    - Netmask: `255.255.255.224`
    - Default Gateway: `199.1.1.65`
- D6: `199.1.1.96/27`
    - Net ID: `199.1.1.96`
    - Broadcast: `199.1.1.127`
    - Netmask: `255.255.255.224`
    - Default Gateway: `199.1.1.97`

### EX2

Question:

Given:
- Class C IP: `203.140.10.0/24`
- 4 Departments with 60 computers each

> [!TIP]  
> Destination IP Address = Sender IP Address AND Netmask, then check
> with the Net ID. If not in every Net ID in the Router, then it directs
> to the ISP.

### Homework

Question:

Given:
- Class A IP: `100.10.10.0/23`
- 8 Departments with maximize amount of computers equally
