.data
	arr: .word 1, 5, 7, 3, 2, 4, 6, 7, 12, 1
	arr_length: .word 10
	
.text
	la $t0, arr
	lw $t1, 16($t0)
	div $t4, $t1, 2
	mfhi $t4
	beq $t4, 0, even
	even: add $s0, $s0, $t1
	
	lw $t1, 20($t0)
	add $s0, $s0, $t1
	
	lw $t1, 24($t0)
	add $s0, $s0, $t1

	lw $t1, 32($t0)
	add $s0, $s0, $t1