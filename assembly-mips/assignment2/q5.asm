.data
	Arr: .word 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20
	result: .asciiz "Sum of odd indexes is: "
	
.text
	la $s0, Arr
	lw $t1, 0($s0)
	add $t0, $t0, $t1
	lw $t1, 8($s0)
	add $t0, $t0, $t1
	lw $t1, 16($s0)
	add $t0, $t0, $t1
	lw $t1, 24($s0)
	add $t0, $t0, $t1
	lw $t1, 32($s0)
	add $t0, $t0, $t1
	lw $t1, 40($s0)
	add $t0, $t0, $t1
	lw $t1, 48($s0)
	add $t0, $t0, $t1
	lw $t1, 56($s0)
	add $t0, $t0, $t1
	lw $t1, 64($s0)
	add $t0, $t0, $t1
	lw $t1, 72($s0)
	add $t0, $t0, $t1
	
	li $v0, 4
	la $a0, result
	syscall
	
	li $v0, 1
	la $a0, ($t0)
	syscall