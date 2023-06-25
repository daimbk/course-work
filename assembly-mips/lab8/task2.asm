.data
	arr1: .word 1, 2, 3, 4, 5
	arr2: .word 6, 7, 8, 9, 0
	arr3: .word 0, 0, 0, 0, 0	
	
.text
	la $t0, arr1
	la $t1, arr2
	la $t2, arr3
	
	lw $s0, 0($t0)
	lw $s1, 0($t1)
	add $s3, $s0, $s1
	sw $s3, 0($t2)
	
	lw $s0, 4($t0)
	lw $s1, 4($t1)
	add $s3, $s0, $s1
	sw $s3, 4($t2)
	
	lw $s0, 8($t0)
	lw $s1, 8($t1)
	add $s3, $s0, $s1
	sw $s3, 8($t2)
	
	lw $s0, 12($t0)
	lw $s1, 12($t1)
	add $s3, $s0, $s1
	sw $s3, 12($t2)
	
	lw $s0, 16($t0)
	lw $s1, 16($t1)
	add $s3, $s0, $s1
	sw $s3, 16($t2)
	
	lw $t0, 0($t2)
	lw $t1, 8($t2)