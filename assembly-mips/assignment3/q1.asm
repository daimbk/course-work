.data
	numbers: .word 0 0 0 0 0 0 0 0 0 0
	input_prompt: .asciiz "Enter a positive number: "
	wrong: .asciiz "Input should be positive number only. Enter again: "
	minimum: .asciiz "Minimum number is: "
	maximum: .asciiz "\nMaximum number is: "
	average: .asciiz "\nAverage: "
	
.text
	li $t1, 0 # initialize min
	li $t2, 0 # initialize max
	li $t3, 0 # initialize average
	li $s0, 0 # counter
	la $t0, numbers # load array
	
	input_loop:
		beq $s0, 10, endloop
		li $v0, 4
		la $a0, input_prompt
		syscall
		
		# read input
		input: la $v0, 5
		syscall
		
		# check if input is a pos num
		j check_input
		
		# min
		continue: beqz $t1, first_min # if its first input set min to it
		blt $v0, $t1, min  # else check
		j continue2
		min: la $t1, ($v0)
			
		#max
		continue2: bgt $v0, $t2, max
		
		store: add $t3, $t3, $v0 # sum for average
		sw $v0, ($t0) # store input in arr
		addi $t0, $t0, 4 # point to next arr element
		addi $s0, $s0, 1 # inc counter
		j input_loop
		
	check_input:
		bgtz $v0, continue
		li $v0, 4 # print re-input prompt
		la $a0, wrong
		syscall
		j input
		
	first_min:
		la $t1, ($v0)
		j continue2
	
	max: 
		la $t2, ($v0)
		j store
		
		
	endloop:
		# print min
		li $v0, 4
		la $a0, minimum
		syscall
		li $v0, 1
		la $a0, ($t1)
		syscall
		
		# print max
		li $v0, 4
		la $a0, maximum
		syscall
		li $v0, 1
		la $a0, ($t2)
		syscall
		
		# find and print avg
		div $t3, $t3, 10
		li $v0, 4
		la $a0, average
		syscall
		li $v0, 1
		la $a0, ($t3)
		syscall
		
		# end
		li $v0, 10
		syscall