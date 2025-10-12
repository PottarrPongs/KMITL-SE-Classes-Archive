@ ARM 32-bit Assembly for Raspberry Pi: Random Numbers [0-9] with One-Time /dev/urandom Seed

.equ GRID_SIZE, 10
.equ LCG_A, 1103515245        @ Multiplier for LCG (from glibc)
.equ LCG_C, 12345             @ Increment for LCG
.equ LCG_M, 2147483648       @ Modulus (2^31 for long period)

.data
urandom_path: .asciz "/dev/urandom"
random_seed_buffer: .space 4  @ 4 bytes for 32-bit seed
prng_state: .word 0           @ Store LCG state
output_buffer: .space 1
newline: .ascii "\n"

.text
@ Subroutine: init_random
@ Description: Reads 4 bytes from /dev/urandom to seed the PRNG.
@ Returns: 0 on success, -1 on error in r0.
init_random:
    push {r4, lr}
    ldr r0, =urandom_path     @ Filename pointer
    mov r1, #0                @ O_RDONLY
    mov r2, #0                @ Mode
    mov r7, #5                @ SYS_OPEN
    svc 0
    mov r4, r0                @ Store file descriptor
    cmp r4, #0
    blt init_error            @ If negative, error

    @ Read 4 bytes for seed
    mov r0, r4
    ldr r1, =random_seed_buffer
    mov r2, #4
    mov r7, #3                @ SYS_READ
    svc 0
    cmp r0, #4
    bne close_and_error       @ If read didn't return 4, error

    @ Close /dev/urandom
    mov r0, r4
    mov r7, #6                @ SYS_CLOSE
    svc 0

    @ Load 4-byte seed and store in prng_state
    ldr r1, =random_seed_buffer
    ldr r0, [r1]              @ Load 32-bit random value
    ldr r1, =prng_state
    str r0, [r1]              @ Initialize PRNG state
    mov r0, #0                @ Success
    pop {r4, pc}

close_and_error:
    mov r0, r4
    mov r7, #6                @ SYS_CLOSE
    svc 0
init_error:
    mov r0, #-1
    pop {r4, pc}

@ Subroutine: generate_one_random_number
@ Description: Generates a single random number between 0 and 9 using LCG.
@ Returns: The random number is in r0.
generate_one_random_number:
    push {r4, lr}
    ldr r4, =prng_state
    ldr r0, [r4]              @ r0 = current state

    @ Apply LCG: state = (a * state + c) mod m
    ldr r1, =LCG_A            @ r1 = a
    mul r2, r0, r1            @ r2 = a * state
    ldr r1, =LCG_C            @ r1 = c
    add r2, r2, r1            @ r2 = a * state + c
    ldr r1, =LCG_M            @ r1 = m
    udiv r3, r2, r1           @ r3 = quotient
    mls r2, r3, r1, r2        @ r2 = (a * state + c) mod m

    @ Store new state
    str r2, [r4]              @ Update prng_state

    @ Rejection sampling for uniform [0-9]
    mov r1, #2147483640       @ Largest multiple of 10 <= LCG_M
    cmp r2, r1
    bge generate_one_random_number  @ Retry if r2 >= 2147483640
    mov r1, #GRID_SIZE        @ r1 = 10
    udiv r3, r2, r1           @ r3 = quotient
    mls r0, r3, r1, r2        @ r0 = remainder (0-9)

    pop {r4, pc}

@ Main program
.global _start
_start:
    @ Initialize PRNG
    bl init_random
    cmp r0, #-1
    beq exit_error

    @ Generate and print 10 random numbers
    mov r4, #10               @ Loop counter
print_loop:
    bl generate_one_random_number
    add r0, r0, #'0'          @ Convert to ASCII ('0'-'9')
    ldr r1, =output_buffer
    strb r0, [r1]             @ Store in buffer

    @ Write to stdout
    mov r0, #1                @ stdout
    ldr r1, =output_buffer
    mov r2, #1
    mov r7, #4                @ SYS_WRITE
    svc 0

    @ Print newline
    mov r0, #1
    ldr r1, =newline
    mov r2, #1
    mov r7, #4
    svc 0

    subs r4, r4, #1
    bne print_loop

    @ Exit
    mov r0, #0
    b exit
exit_error:
    mov r0, #1                @ Exit code 1 on error
exit:
    mov r7, #1                @ SYS_EXIT
    svc 0
