.data
prompt: .asciiz "Enter the value of n: "
result: .asciiz "The first n odd numbers and their sum: "
single_space: .asciiz " "
next_line: .asciiz "\n"

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
  
  # Initialize the sum to zero
  li $t1, 0
  
  # Initialize the counter to one
  li $t2, 1
  
  # Print the result header
  li $v0, 4
  la $a0, result
  syscall
  
  # Loop to display the odd numbers and calculate the sum
  loop:
    # Print the current odd number
    li $v0, 1
    move $a0, $t2
    syscall
    
    # Print a space
    li $v0, 4
    la $a0, single_space
    syscall
    
    # Add the current odd number to the sum
    add $t1, $t1, $t2
    
    # Increment the counter by 2 to get the next odd number
    addi $t2, $t2, 2
    
    # Decrement n
    addi $t0, $t0, -1
    
    # Check if n is greater than zero, continue the loop
    bgtz $t0, loop
    
  # Print a new line
  li $v0, 4
  la $a0, next_line
  syscall
  
  # Print the sum
  li $v0, 1
  move $a0, $t1
  syscall
  
  # Exit the program
  li $v0, 10
  syscall
