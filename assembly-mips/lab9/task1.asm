.data
	first_num: .asciiz "Enter the first number: "
	sec_num: .asciiz "Enter the second number: "
	third_num: .asciiz "Enter the third number: "
	result: .asciiz "The median of three numbers is: "
	
.text	
	# input first num
	li $v0, 4
	la $a0, first_num
	syscall
	
	li $v0, 5
	syscall
	move $t0, $v0
	
	# input second num
	li $v0, 4
	la $a0, sec_num
	syscall
	
	li $v0, 5
	syscall
	move $t1, $v0
	
	# input third num
	li $v0, 4
	la $a0, third_num
	syscall
	
	li $v0, 5
	syscall
	move $t2, $v0
	
	li $v0, 4
	median: bgt $t1, $t0, second_condition
	third_condition: bgt $t0, $t2, median_isfirst
	j median_isthird
	
	second_condition: bgt $t2, $t1, median_issecond
	j third_condition
	
	median_isfirst: la $a0, result
	syscall
	li $v0, 1
	move $a0, $t0
	syscall
	j end
	
	median_issecond: la $a0, result
	syscall
	li $v0, 1
	move $a0, $t1
	syscall
	j end
	
	median_isthird: la $a0, result
	syscall
	li $v0, 1
	move $a0, $t2
	syscall
	j end
	
	end: li $v0, 10
	syscall