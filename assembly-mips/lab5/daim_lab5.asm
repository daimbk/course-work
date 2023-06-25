.data
	arr1: .word 1,2,3,4,5,6,7,8,9,10
	var1: .word 0
	var2: .word 0
	var3: .word 0
	
	input_prompt: .asciiz "Enter integer: "
	result: .asciiz "Result of div: "
	
.text
	# task 1
	li $t1, 5
	li $t2, 10
	move $t3, $t2
	move $t2, $t1
	move $t1, $t3
	
	# task 2
	la $t1, arr1
	lw $t2, 20($t1)
	lw $t3, 36($t1)
	add $s1, $t2, $t3
	sw $s1, 28($t1)
	
	# task 3
	li $v0, 4
	la $a0, input_prompt
	syscall
	
	li $v0, 5 #read input
	syscall
	move $t0, $v0
	
	li $v0, 4
	la $a0, input_prompt
	syscall
	
	li $v0, 5 #read input
	syscall
	move $t1, $v0 
	
	add $t2, $t0, $t1
	li $s0, 2
	div $t2, $t2, $s0
	sw $t2, var3
	
	li $v0, 4
	la $a0, result
	syscall
	li $v0, 1
	lw $s1, var3
	move $a0, $s1
	syscall
	
	li $v0, 10
	syscall