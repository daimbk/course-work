.data
prompt: .asciiz "Enter the value of n: "
result: .asciiz "The sum of the series is: "

.text
main:
  # Prompt the user for the value of n
  li $v0, 4
  la $a0, prompt
  syscall
  
  # Read user input for n
  li $v0, 5
  syscall
  move $t0, $v0  # Store n in $t0
  
  # Calculate the sum of the series
  li $t1, 0  # Initialize the sum to zero
  li $t2, 1  # Initialize the counter to 1
  
  loop:
    bgt $t2, $t0, end_loop  # End the loop if counter exceeds n
    
    mul $t3, $t2, $t2       # Calculate the square of the counter
    add $t1, $t1, $t3       # Add the square to the sum
    
    addi $t2, $t2, 1       # Increment the counter
    j loop
    
  end_loop:
    # Print the result
    li $v0, 4
    la $a0, result
    syscall
    
    move $a0, $t1
    li $v0, 1
    syscall
    
    # Exit the program
    li $v0, 10
    syscall
