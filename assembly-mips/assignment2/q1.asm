.data
	first_prompt: .asciiz "Enter first number: "
	sec_prompt: .asciiz "Enter second number: "
	third_prompt: .asciiz "Enter third number: "
	
	bigger: .asciiz "sum is greater than 10"
	not_greater: .asciiz "sum is less than or equal to 10"
	
.text
	# print prompt
	li $v0, 4
	la $a0, first_prompt
	syscall
	
	# read integer
	li $v0, 5
	syscall
	la $t0, ($v0)
	
	li $v0, 4
	la $a0, sec_prompt
	syscall
	
	# read integer
	li $v0, 5
	syscall
	la $t1, ($v0)
	
	li $v0, 4
	la $a0, third_prompt
	syscall
	
	# read integer
	li $v0, 5
	syscall
	la $t2, ($v0)
	
	# add numbers
	add $t0, $t0, $t1
	add $t0, $t0, $t2
	
	li $v0, 4
	bgt $t0, 10, greater
	la $a0, not_greater
	
	b exit
	greater: la $a0, bigger
	exit: syscall