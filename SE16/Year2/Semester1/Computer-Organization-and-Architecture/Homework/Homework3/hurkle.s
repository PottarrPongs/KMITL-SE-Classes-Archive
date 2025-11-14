.equ GRID_SIZE, 10
.equ LCG_A, 1103515245        @ Multiplier for LCG (from glibc)
.equ LCG_C, 12345             @ Increment for LCG
.equ LCG_M, 2147483648       @ Modulus (2^31 for long period)

.section .data
gx: .word 0
gy: .word 0
hx: .word 0
hy: .word 0
guess_amount: .word 0
input_buf: .space 10
output_buf: .space 11

guess_prompt: .ascii "Enter X Y: "
guess_prompt_len = . - guess_prompt
invalid_input: .ascii "Invalid input\n"
invalid_input_len = . - invalid_input

too_high: .ascii "Too high!\n"
too_high_len = . - too_high
too_low: .ascii "Too low!\n"
too_low_len = . - too_low
too_left: .ascii "Too far left!\n"
too_left_len = . - too_left
too_right: .ascii "Too far right!\n"
too_right_len = . - too_right
very_close: .ascii "You are very close!\n"
very_close_len = . - very_close

win_1: .ascii "You found the Hurkle in "
win_1_len = . - win_1
win_2: .ascii " guesses!\n"
win_2_len = . - win_2
lose_1: .ascii "You ran out of guesses! The Hurkle was at ("
lose_1_len = . - lose_1
lose_2: .ascii ", "
lose_2_len = . - lose_2
lose_3: .ascii ")\n"
lose_3_len = . - lose_3

newline: .ascii "\n"

urandom_path: .asciz "/dev/urandom"
random_seed_buffer: .space 4  @ 4 bytes for 32-bit seed
prng_state: .word 0           @ Store LCG state

.section .text
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

@ Return a random number into r0
generate_one_random_number:
    push {r4, lr}
    ldr r4, =prng_state
    ldr r0, [r4]

    @ Apply LCG: state = (a * state + c) mod m
    ldr r1, =LCG_A
    mul r2, r0, r1
    ldr r1, =LCG_C
    add r2, r2, r1
    ldr r1, =LCG_M
    udiv r3, r2, r1
    mls r2, r3, r1, r2

    @ Store new state
    str r2, [r4]              @ Update prng_state

    @ Rejection sampling for uniform [0-9]
    mov r1, #2147483640       @ Largest multiple of 10 <= LCG_M
    cmp r2, r1
    bge generate_one_random_number  @ Retry if r2 >= 2147483640
    mov r1, #GRID_SIZE
    udiv r3, r2, r1
    mls r0, r3, r1, r2        @ r0 = remainder (0-9)

    pop {r4, pc}
    
init_game:
	push {lr}
	bl init_random
	cmp r0, #-1
    beq exit_error
    
    @ generate hx
    bl generate_one_random_number
    ldr r1, =hx
    str r0, [r1]
    
    @ generate hy
    bl generate_one_random_number
    ldr r1, =hy
    str r0, [r1]
    
    ldr r1, =guess_amount
    mov r0, #0
    str r0, [r1]
    
    pop {pc}
    
itoa:
    push {lr}
    ldr r0, [r1]
    add r0, r0, #'0'
    ldr r1, =output_buf
    str r0, [r1]
    mov r2, #1
    pop {pc}
    
print_string:
	mov r7, #4
	mov r0, #1
	svc #0
	bx lr

.global _start
_start:
	bl init_game
	
game_loop:
    ldr r1, =guess_amount
    ldr r0, [r1]
    add r0, r0, #1
    cmp r0, #10
    bgt game_over

    str r0, [r1]

get_player_guess:
    ldr r1, =guess_prompt
    mov r2, #guess_prompt_len
    bl print_string

    mov r7, #3
    mov r0, #0
    ldr r1, =input_buf
    mov r2, #10
    svc #0

    ldr r1, =input_buf
    ldrb r2, [r1]
    cmp r2, #'0'
    blt input_error
    cmp r2, #'9'
    bgt input_error

    ldr r1, =input_buf + 1
    ldrb r2, [r1]
    cmp r2, #' '
    bne input_error

    ldr r1, =input_buf + 2
    ldrb r2, [r1]
    cmp r2, #'0'
    blt input_error
    cmp r2, #'9'
    bgt input_error

    ldr r1, =input_buf + 3
    ldrb r2, [r1]
    cmp r2, #'\n'
    bne input_error

    ldr r1, =input_buf
    ldrb r4, [r1]
    sub r4, r4, #'0'
    ldr r1, =gx
    str r4, [r1]

    ldr r1, =input_buf + 2
    ldrb r4, [r1]
    sub r4, r4, #'0'
    ldr r1, =gy
    str r4, [r1]

    b give_feedback

input_error:
    ldr r1, =invalid_input
    mov r2, #invalid_input_len
    bl print_string

    b get_player_guess

give_feedback:
    ldr r1, =gx
    ldr r3, [r1]
    ldr r1, =gy
    ldr r4, [r1]
    ldr r1, =hx
    ldr r5, [r1]
    ldr r1, =hy
    ldr r6, [r1]

    sub r1, r3, r5
    sub r2, r4, r6

    cmp     r1, #0
    rsblt   r1, r1, #0
    cmp     r2, #0
    rsblt   r2, r2, #0

    add r0, r1, r2

    cmp r0, #0
    beq game_win
    cmp r0, #2
    bgt compare_x

vclose:
    ldr r1, =very_close
    mov r2, #very_close_len
    bl print_string

compare_x:
    ldr r1, =gx
    ldr r3, [r1]
    ldr r1, =hx
    ldr r4, [r1]
    cmp r3, r4
    blt less_x
    beq compare_y

more_x:
    ldr r1, =too_right
    mov r2, #too_right_len
    bl print_string
    b compare_y

less_x:
    ldr r1, =too_left
    mov r2, #too_left_len
    bl print_string

compare_y:
    ldr r1, =gy
    ldr r3, [r1]
    ldr r1, =hy
    ldr r4, [r1]
    cmp r3, r4
    blt less_y
    beq game_loop

more_y:
    ldr r1, =too_high
    mov r2, #too_high_len
    bl print_string
    b game_loop

less_y:
    ldr r1, =too_low
    mov r2, #too_low_len
    bl print_string
    b game_loop

game_win:
    ldr r1, =win_1
    mov r2, #win_1_len
    bl print_string

    ldr r1, =guess_amount
    bl itoa
    bl print_string

    ldr r1, =win_2
    mov r2, #win_2_len
    bl print_string

    mov r0, #0
    b exit

game_over:
    ldr r1, =lose_1
    mov r2, #lose_1_len
    bl print_string

    ldr r1, =hx
    bl itoa
    bl print_string

    ldr r1, =lose_2
    mov r2, #lose_2_len
    bl print_string

    ldr r1, =hy
    bl itoa
    bl print_string

    ldr r1, =lose_3
    mov r2, #lose_3_len
    bl print_string

    mov r0, #0
    b exit

exit_error:
    mov r0, #1                @ Exit code 1 on error
exit:
    mov r7, #1                @ SYS_EXIT
    svc #0
