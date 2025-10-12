.section .data
prompt_name: .ascii "What is your name? "
len_prompt_name = . - prompt_name
prompt_year: .ascii "What year were you born? "
len_prompt_year = . - prompt_year
greeting: .ascii "Hello "
len_greeting = . - greeting
comma: .ascii ", you are "
len_comma = . - comma
years: .ascii " years old.\n"
len_years = . - years
name_buf: .space 101
year_buf: .space 11
age_buf: .space 11

.section .text
.global _start

_start:
    // Prompt for name
    mov r7, #4
    mov r0, #1
    ldr r1, =prompt_name
    mov r2, #len_prompt_name
    svc #0

    // Read name
    mov r7, #3
    mov r0, #0
    ldr r1, =name_buf
    mov r2, #100
    svc #0

    // Save name length and remove newline
    mov r3, r0          // r3 = length including newline
    ldr r1, =name_buf
    mov r4, r1          // r4 = start of name_buf for length calc
    mov r5, #0          // r5 = actual string length
find_name_len:
    ldrb r2, [r4]
    cmp r2, #0          // check for null
    beq name_len_done
    cmp r2, #10         // check for newline
    beq name_len_done
    add r5, r5, #1
    add r4, r4, #1
    cmp r5, r3          // ensure we don't exceed read length
    blt find_name_len
name_len_done:
    mov r2, #0
    strb r2, [r4]       // null terminate at newline or end
    mov r8, r5          // r8 = actual name length (preserve)

    // Prompt for year
    mov r7, #4
    mov r0, #1
    ldr r1, =prompt_year
    mov r2, #len_prompt_year
    svc #0

    // Read year
    mov r7, #3
    mov r0, #0
    ldr r1, =year_buf
    mov r2, #10
    svc #0

    // Convert year to integer (atoi)
    ldr r1, =year_buf
    mov r4, #0          // result
atoi_loop:
    ldrb r2, [r1]
    add r1, #1
    cmp r2, #'0'
    blt atoi_done
    cmp r2, #'9'
    bgt atoi_done
    sub r2, #'0'
    mov r3, r4
    lsl r4, #3          // r4 * 8
    lsl r3, #1          // r3 * 2
    add r4, r4, r3      // r4 = old_r4 * 10
    add r4, r4, r2      // add digit
    b atoi_loop
atoi_done:

    // Calculate age
    mov r5, #2025
    sub r5, r5, r4      // age = 2025 - birth_year

    // Convert age to string (itoa)
    ldr r1, =age_buf + 9
    mov r2, #0
    strb r2, [r1]       // null terminate
    mov r0, #10         // base
itoa_loop:
    sub r1, r1, #1
    udiv r3, r5, r0     // quotient
    mls r2, r0, r3, r5  // remainder = r5 - (quotient * 10)
    add r2, r2, #'0'
    strb r2, [r1]
    mov r5, r3
    cmp r5, #0
    bne itoa_loop

    // Save age string start pointer
    mov r6, r1          // r6 = start of age string

    // Output greeting: "Hello "
    mov r7, #4
    mov r0, #1
    ldr r1, =greeting
    mov r2, #len_greeting
    svc #0

    // Output name
    mov r7, #4
    mov r0, #1
    ldr r1, =name_buf
    mov r2, r8          // use preserved name length
    svc #0

    // Output ", you are "
    mov r7, #4
    mov r0, #1
    ldr r1, =comma
    mov r2, #len_comma
    svc #0

    // Output age
    mov r7, #4
    mov r0, #1
    mov r1, r6          // restore age string start
    ldr r4, =age_buf + 9
    sub r2, r4, r1      // r2 = length
    svc #0

    // Output " years old.\n"
    mov r7, #4
    mov r0, #1
    ldr r1, =years
    mov r2, #len_years
    svc #0

    // Exit
    mov r7, #1
    mov r0, #0
    svc #0
    