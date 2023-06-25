.data
	# Question 1
	a: .word 5
	b: .word 2
	c: .word 3
	x: .word 0
	y: .word 0
	
	input_prompt: .asciiz "Enter a value for x: "
	result_prompt: .asciiz "The result of the quadratic equation is "
	
	# Question 2
	input1: .asciiz "\nEnter first number: "
	input2: .asciiz "Enter second number: "
	
	result: .asciiz "Swapped Values: "
	first: .asciiz "\nFirst Number: "
	second: .asciiz "\nSecond Number: "
	
.text
	# Question 1
	li $v0, 4
	la $a0, input_prompt
	syscall
	
	li $v0, 5 #read input
	syscall
	sw $v0, x
	
	# perform quadratic operations
	lw $s1, a
	lw $s2, b
	lw $s3, c
	lw $s4, x
	# a * x
	mul $t0, $s1, $s4
	# a * x * x
	mul $t0, $t0, $s4
	# b * x
	mul $t1, $s2, $s4
	# b* x + c
	add $t1, $t1, $s3
	# a * x * x + b * x + c
	add $t0, $t0, $t1
	
	sw $t0, y
	
	# print result
	li $v0, 4
	la $a0, result_prompt
	syscall
	li $v0, 1
	lw $a0, y
	syscall
	
	# Question 2
	li $v0, 4
	la $a0, input1
	syscall
	
	li $v0, 5 #read input 1
	syscall
	move $s0, $v0
	
	li $v0, 4
	la $a0, input2
	syscall
	
	li $v0, 5 #read input 2
	syscall
	move $s1, $v0
	
	# swap using XOR
	xor $s0, $s0, $s1
	xor $s1, $s0, $s1
	xor $s0, $s0, $s1
	
	# print results
	li $v0, 4
	la $a0, result
	syscall
	
	la $a0, first
	syscall
	li $v0, 1
	la $a0, ($s0)
	syscall
	
	li $v0, 4
	la $a0, second
	syscall
	
	li $v0, 1
	la $a0, ($s1)
	syscall