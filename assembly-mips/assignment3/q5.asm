.data
    numbers: .word 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    input_prompt: .asciiz "Enter a positive number: "
    wrong: .asciiz "Input should be a positive number only. Enter again: "
    minimum: .asciiz "\nMinimum number is: "
    maximum: .asciiz "\nMaximum number is: "
    average: .asciiz "\nAverage: "

.text
main:
    la $a0, numbers  # Array address
    li $a1, 10      # Array size
    
    # Call the find_min_max_avg procedure
    jal find_min_max_avg
    
    # Exit program
    li $v0, 10
    syscall

find_min_max_avg:
    li $t1, 0       # initialize min
    li $t2, 0       # initialize max
    li $t3, 0       # initialize sum
    li $t4, 0       # initialize average
    li $s0, 0       # counter
    move $t0, $a0   # load array address

    input_loop:
        beq $s0, $a1, endloop
        
        # Print input prompt
        li $v0, 4
        la $a0, input_prompt
        syscall
        
        # Read input
        li $v0, 5
        syscall
        
        # Check if input is a positive number
        j check_input
        
    continue:
        # Minimum
        beqz $t1, first_min  # If it's the first input, set min to it
        blt $v0, $t1, min    # Else check
        j continue2
    min:
        move $t1, $v0
        
    continue2:
        # Maximum
        bgt $v0, $t2, max
    
    store:
        add $t3, $t3, $v0  # Sum for average
        sw $v0, ($t0)      # Store input in array
        addi $t0, $t0, 4  # Point to next array element
        addi $s0, $s0, 1  # Increment counter
        j input_loop
        
    check_input:
        bgtz $v0, continue
        li $v0, 4         # Print re-input prompt
        la $a0, wrong
        syscall
        j input_loop
        
    first_min:
        move $t1, $v0
        j continue2
        
    max:
        move $t2, $v0
        j store
        
    endloop:
        # Print min
        li $v0, 4
        la $a0, minimum
        syscall
        li $v0, 1
        move $a0, $t1
        syscall
        
        # Print max
        li $v0, 4
        la $a0, maximum
        syscall
        li $v0, 1
        move $a0, $t2
        syscall
        
        # Calculate and print average
        div $t3, $a1
        mflo $t4

        # Print average
        li $v0, 4
        la $a0, average
        syscall
        li $v0, 1
        move $a0, $t4
        syscall

        jr $ra