.data
	input: .asciiz "Enter a number: "
	result: .asciiz "Answer is: "
	number: .word 0
	number2: .word 0
	
.text
	main: li $v0, 4
	la $a0, input
	syscall
	
	# read input
	li $v0, 5
	syscall
	sw $v0, number
	
	# call factorial
	lw $t0, number
	jal factorial
	move $s2, $s0 # store result in s2
	
	# get second number
	li $v0, 4
	la $a0, input
	syscall
	
	# read input
	li $v0, 5
	syscall
	sw $v0, number2
	
	# call factorial
	lw $t0, number2
	jal factorial
	move $s3, $s0 # store result in s3
	
	# add answers and print
	add $s2, $s2, $s3
	li $v0, 4
	la $a0, result
	syscall
	li $v0, 1
	move $a0, $s2
	syscall
	
	j end

	factorial:
    		li $s0, 1
    		loop: beq $t0, $zero, endfunc
        	mul $s0, $s0, $t0
        	addi $t0, $t0, -1
        	j loop
    	endfunc: jr $ra
	
	end: li $v0, 10
	syscall