.data
	# part 1
	x: .word 0
	y: .word 0
	z: .word 0
	y_prompt: .asciiz "Enter y: "
	z_prompt: .asciiz "Enter z: "
	result_x: .asciiz "The result x is: "
	
	# part 2
	a: .word 0
	b: .word 0
	c: .word 0
	b_prompt: .asciiz "\n\nEnter b: "
	c_prompt: .asciiz "Enter c: "
	result_a: .asciiz "The result a is: "
	
.text
	# part 1: x = y + z + 10
	# get y
	li $v0, 4
	la $a0, y_prompt
	syscall
	
	li $v0, 5
	syscall
	sw $v0, y
	
	# get z
	li $v0, 4
	la $a0, z_prompt
	syscall
	
	li $v0, 5
	syscall
	sw $v0, z
	
	# add
	lw $t0, y
	lw $t1, z
	add $t0, $t0, $t1
	addi $t0, $t0, 10
	sw $t0, x
	
	# print result
	li $v0, 4
	la $a0, result_x
	syscall
	
	li $v0, 1
	lw $t0, x
	la $a0, ($t0)
	syscall
	
	# part 2: a = (b-3) + 2c
	# get b
	li $v0, 4
	la $a0, b_prompt
	syscall
	
	li $v0, 5
	syscall
	sw $v0, b
	
	# get c
	li $v0, 4
	la $a0, c_prompt
	syscall
	
	li $v0, 5
	syscall
	sw $v0, c
	
	# solve
	lw $t0, b
	lw $t1, c
	subi $t0, $t0, 3
	sll $t1, $t1, 1
	add $t0, $t0, $t1
	sw $t0, a
	
	# print result
	li $v0, 4
	la $a0, result_a
	syscall
	
	li $v0, 1
	lw $t0, a
	la $a0, ($t0)
	syscall