.data
	prompt: .asciiz "Enter an integer between 0 and 15: "
	result: .asciiz "Result of 2s complement: "
	
.text
	# get input
	li $v0, 4
	la $a0, prompt
	syscall
	
	li $v0, 5
	syscall
	la $t0, ($v0)
	# set all bits of t1 to 1
	li $t1, 15
	xor $t0, $t0, $t1
	add $t0, $t0, 1
	
	# print result
	li $v0, 4
	la $a0, result
	syscall
	
	li $v0, 1
	la $a0, ($t0)
	syscall