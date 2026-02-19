# Lecture 3

## Physical Layer

### Bandwidth

Upload Speed: The higher the better  
Download Speed: The higher the better  
Round Trip Time (RTT): The lower the better

> [!IMPORTANT]  
> Why use Bit/Second (bps) not Byte/Second (Bps)  
> - Answer: Because we send the data through the network bit by bit


- Bandwidth is finite
- Bandwidth is not free
- Bandwidth is a key factor in analyzing network performance, designing
new networks, and understanding the Internet.
- The demand of bandwidth is ever increasing
- Bandwidth is the maximum (but mostly get lower than the maximum).


### Throughput

Throughput is IRL version of bandwidth. (Therefore, bandwidth is the maximum
value of the throughput.)

Why throughput is lower than bandwidth?
- Answer:
    - Internet working devices
    - Type of data being transferred
    - Network Topology
    - Number of users in the network
    - User computer
    - Server computer
    - Power conditions

### 3 - Transmission Media

- Copper Media (Transfer Electricity)
    - Used in almost every LAN has copper media
    - Cable specification
        - 10 BASE-T
            - 10 $\rightarrow$ 10 Mbps
            - Base $\rightarrow$ Baseband (AKA LAN)
            - T $\rightarrow$ Maximum length (T is No longer than 100 m
            (performance will drop and more error after surpass 100 m))
        - 100 BASE-T
            - 100 $\rightarrow$ 100 Mbps
        - 1000 BASE-T (Gigabit Ethernet)
            - 1000 $\rightarrow$ 1 Gbps
        - 10 BASE5
        - 10 BASE2
    - Categories
        - Coaxial Cable
            - Speed and Throughput 10-100 Mbps
            - Max Cable Length 500 m
            - Cheaper but obsolete.
        - Twisted-Pair Cable
            - STP (Shielded Twisted-Pair) $\rightarrow$ Has a metal
            sheet cover on every pair to protect from Electro-Magnetic
            Interference (EMI) causing error. Mostly use in the same
            pipe with the power line due to the Interference from the
            Electro-Magnetic field from the power line.
            - UTP (Unshielded Twisted-Pair) $\rightarrow$ No metal sheet
            covering. Use when no EMI nearby.
            - Speed and Throughput 10 - 100 - 1000 - 2500 - 5000 - 10000 Mbps
            - Max Length 100 m
            - Standard Color of the lines
                - Yellow, Green $\rightarrow$ TX, RX
                - Blue, Brown $\rightarrow$ Power Over Ethernet Line
            - Why the line inside twisted?
                - Answer: To reduce crosstalk between the pairs
                    - If not twisted, the parallel lines will create
                    error from the Electro-Magnetic field from the line
                    next to the refer line.
                    - If twisted, it reduce the Electro-Magnetic field
                    (by the property of wave) the Electro-Magnetic field
                    will mostly cancelled by 60% approximately.
    - Ethernet Cable Standard
        - TIA/EIA-568-AB
            - A method for wiring
            - RJ45 Connector (LAN Connector) (has 8 pins for 8 lines)
            - CAT 6 (Category  6)
        - Cables Connection
            - Straight Through Cables (Use in the different level connecting)
                - TX $\iff$ TX and RX $\iff$ RX $\rightarrow$ E.g. Computer $\implies$ Switch
            - Crossover Cables (Rollover Cables) (Use in the same level connecting)
                - Swap RX TX $\rightarrow$ RX $\implies$ TX or TX $\implies$ RX, For Computer $\iff$ Computer
        - Power Over Ethernet (POE)
        - Order of cables
            - 1 TX+
            - 2 TX-
            - 3 RX+
            - 6 RX-
            - 7,8 POE+
            - 4,5 POE-
- Optical Media (Transfer Light)
    - Components
        - Light Source
        - Transmission Media
        - Detector
        - Detect from light and dark to binary (`1` is light, `0` 
        is dark.).
        - Mode
            - Multi Mode
                - Slower and can not go that long due to bouncing in
                the cable
            - Single Mode
                - Faster and can go longer
        - Connector
            - LC $\rightarrow$ Lucent Connector
                - Has the lit
                - 500 mating cycles
            - SC $\rightarrow$ Small/Simple Connector
                - 1000 mating cycles
            - FC $\rightarrow$ Fiber Optic Connector
                - 500 mating cycles
        - Connector Contact
            - PC $\rightarrow$ Physical Contact
                - No angle
                - Obsolete due to the reflection might interfere the
                other light source coming through
                - Return lost -40dB
            - APC $\rightarrow$ Angled Physical Contact (Green)
                - 8-Degree Angle
                - The best one
                - Return lost -60dB
            - UPC $\rightarrow$ Ultra Physical Contact (Blue)
                - Rounded curve on the tip
                - Return lost -50dB


- Wireless Media (Transfer Wave)

> [!NOTE]  
> If you would like to choose cable, choose CAT 6 or newer. CAT 5 is
> is very obsolete and will never guarantee to the real bandwidth.

> [!IMPORTANT]  
> All the Ethernet Cables using outdoor should be black color. Black
> ones have UV coated.

