.global add
.type add, %function
add:
	push {lr}
	add r0, r0, r1
	pop {lr}
	bx lr
