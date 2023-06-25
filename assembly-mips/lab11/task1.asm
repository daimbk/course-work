.data
	prompt: .asciiz "Enter a string: "
	length: .asciiz "Length of string is: "
	input: .space 255
	
	next_line: .asciiz "\n"
	
	string1: .asciiz "Daim"
	string2: .asciiz "Khalid"
	
.text
	#strLen
	# take input
	li $v0, 4
	la $a0, prompt
	syscall
	
	li $v0, 8
	li $a1, 40
	la $a0, input
	syscall
	move $t0, $a0
	
	# set counter
	li $t1, -1
	
	strLen:
		lbu $t3, ($t0)
		addi $t0, $t0, 1
		
		beqz $t3, printStr
		addi $t1, $t1, 1
		
		j strLen
		
	printStr:
		li $v0, 4
		la $a0, length
		syscall
		
		move $a0, $t1
		li $v0, 1
		syscall
		
		li $v0, 4
		la $a0, next_line
		syscall
	
	# strRev	
	addi $t0, $t0, -3
	strRev:
		lbu $t3, ($t0)
		addi $t0, $t0, -1
		
		li $v0, 11
		move $a0, $t3
		syscall
		
		addi $t1, $t1, -1 # length of string becomes counter in this func
		
		beqz $t1, strCat
		j strRev
		
	# strCat
	strCat:
		la $t3, string1
		la $t4, string2
		la $s0, 0 # counter to see how many times pointer moves for t3
		str1:
			lbu $t0, ($t3)		
			beqz $t0, str2
			
			addi $t3, $t3, 1
			addi $s0, $s0, 1 # inc counter
			
			j str1
			
		str2:
			lbu $t1, ($t4)
			beqz $t1, printCat
			
			sb $t1, ($t3)
			addi $t3, $t3, 1
			addi $t4, $t4, 1
			addi $s0, $s0, 1 # inc counter
			
			j str2
			
		printCat:
			sub $t3, $t3, $s0 # set pointer of string to its start
			
			li $v0, 4
			la $a0, next_line
			syscall 
	
			li $v0, 4
			move $a0, $t3
			syscall
			
	# strSplit
	li $t0, 0 # clear registers
	li $t1, 0
	
	li $v0, 4
	la $a0, next_line
	syscall
	
	la $a0, prompt
	syscall
	
	li $v0, 8
	la $a1, 255
	la $a0, input
	syscall
	move $t0, $a0
	
	strSplit:
		lbu $t1, ($t0)
		
        	beqz $t1, end
        	addi $t0, $t0, 1
        
        	li $v0, 11
        	move $a0, $t1
        	syscall       	
        
        	li $a0, '*'
        	syscall
        
        	j strSplit 

		
	end:
		li $v0, 10
		syscall
