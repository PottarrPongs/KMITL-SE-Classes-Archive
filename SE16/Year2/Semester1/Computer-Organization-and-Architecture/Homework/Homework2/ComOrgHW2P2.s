_start:
    LD  R0, =10     @ LD 10 into R0
    ADD R0, #15     @ Add 15 to R0
    ST  R0, [R1]    @ Store result into Memory of R1
    CMP R0          @ Check the value of R0 compare with 0
    BRG b1          @ Branch to b1 if R0 is more than 0
    SWI 0           @ Software interrupt to end the program
clr:
    LD  R0, =0      @ Loads number 0 to R0
    RET  _start     @ Return to _start and rerun until get not greater
