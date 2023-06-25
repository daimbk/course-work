.data
count:   .word 0         # Variable to store the count
buffer: .space 100      # Buffer to store the user input

.text
main:
  li $v0, 8             # Read string syscall code
  la $a0, buffer        # Address of the buffer
  li $a1, 100           # Maximum buffer size
  syscall
  
  la $t0, buffer        # Load the address of the buffer
  li $t1, 0             # Initialize the count
  
  loop:
    lb $t2, ($t0)       # Load a character from the buffer
    
    beqz $t2, end_loop  # End the loop if Enter key is pressed (null character)
    
    blt $t2, 'A', not_capital    # If the character is less than 'A', it's not a capital letter
    bgt $t2, 'Z', not_capital    # If the character is greater than 'Z', it's not a capital letter
    
    addiu $t1, $t1, 1   # Increment the count
    
    not_capital:
      addiu $t0, $t0, 1   # Increment the buffer pointer
      j loop
    
  end_loop:
    sw $t1, count        # Store the count in the 'count' variable
    
    # Exit the program
    li $v0, 10
    syscall