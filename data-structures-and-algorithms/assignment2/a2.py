#===================================
#===================================
# Name   : Daim Bin Khalid
# Roll no: 251686775
# Section: C
# Date   : 13/12/2022
#===================================
#===================================


#------------------------------------
# Node class for a Doubly Linked List
#------------------------------------
class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next
#------------------------------------

import copy

# Stack class
class Stack:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def top(self):
        if self.is_empty():
            return None
        return self._data[-1]

    def push(self, e):
        self._data.append(e)

    def pop(self):
        if self.is_empty():
            return None
        return self._data.pop()


class TextEditor:
    def __init__(self):
        '''
        Predefined member variables. 
        
        WARNING: DO NOT MODIFY THE FOLLOWING VARIABLES
        '''
        
        self.doc = None   # The root of everything. See page 2 for details
        
        #======================
        # Insert your Member
        #   variables here (if any):
        #----------------------

        self.doc = Node(None)
        self.cursor = [-1, -1]

        self.stack = Stack()
        self.redo_stack = Stack()

        #======================
        
#======================
    def goto(self, row, col):
        '''
        Moves the cursor to the location indicated by the 
          row and col parameters
 
        Parameters:
            row --> row number to move to
            col --> column number to move to
        
        Return value:
            None
        '''

        # condition to make sure same values of sheet are not pushed to stack
        if len(self.stack) == 0 or (self.cursor[0] != self.stack.top()[1][0] and self.cursor[1] != self.stack.top()[1][1]):
        # push state to stack for undo and redo operations
            state = [copy.deepcopy(self.doc), copy.deepcopy(self.cursor)]
            self.stack.push(state)

        # assign header for row pointer and assign column pointer
        row_iterator = self.doc
        col_iterator = self.doc.data

        if row >= 0 and col >= 0:
            # change cursor position
            self.cursor = [row, col]

            for _ in range(row):
                # check if required nodes do not exist if not make them
                if row_iterator.next == None:
                    node = Node(None, row_iterator)
                    prev = node
                    row_iterator.next = node
                    row_iterator = row_iterator.next
                # move to next node if it exists
                else:
                    row_iterator = row_iterator.next

            # check if required columns exist if not make them
            if row_iterator.data == None:
                prev = row_iterator
                col_iterator = Node(' ', prev)
                prev = col_iterator
                row_iterator.data = col_iterator
                if col != 0:
                    for _ in range(col):
                        node = Node(' ', prev)
                        prev = node
                        col_iterator.next = node
                        col_iterator = col_iterator.next
            else:
                # build further needed column/s following already existing column
                col_iterator = row_iterator.data
                for _ in range(col):
                    if col_iterator.next == None:
                        prev = col_iterator
                        node = Node(' ', prev)
                        prev = node
                        col_iterator.next = node
                    col_iterator = col_iterator.next

        state = [copy.deepcopy(self.doc), copy.deepcopy(self.cursor)]
        self.stack.push(state)

#======================

#======================
    def forward(self):
        '''
        Moves the cursor one step forward
 
        Parameters:
            None
        
        Return value:
            None
        '''
        
        # check to see if the cursor is in a valid state
        if self.cursor[0] >= 0 and self.cursor[1] >= 0:
            row = self.cursor[0]
            col = self.cursor[1]
            
            # setup row and column iterators
            row_iterator = self.doc
            for _ in range(row):
                row_iterator = row_iterator.next

            col_iterator = row_iterator.data

            # flags to check if at end of line and if next row exists
            next_row_exists = True
            end_of_line = False

            # iterative loop to check if at end of line
            for _ in range(col + 1):
                if col_iterator.next is not None:
                    col_iterator = col_iterator.next
                else:
                    end_of_line = True

            if end_of_line:
                # iterative loop to check if next row exists
                for _ in range(row):
                    if row_iterator.next is not None:
                        row_iterator = row_iterator.next
                    else:
                        next_row_exists = False

                # move cursor to first place of next line if next row exists 
                if next_row_exists:
                    # create a node at first position in line if it doesn't exist
                    if row_iterator.data is None:
                        row_iterator.data = Node(' ', row_iterator)

                self.cursor[0] = row + 1
                self.cursor[1] = 0

            # move cursor one place forward in line if not already at end of line
            else:
                self.cursor[1] = col + 1 

        state = [copy.deepcopy(self.doc), copy.deepcopy(self.cursor)]
        self.stack.push(state)

#======================

#======================
    def back(self):
        '''
        Moves the cursor one step backwards
 
        Parameters:
            None
        
        Return value:
            None
        '''
        
        # check if the cursor is valid
        if self.cursor[0] >= 0 and self.cursor[1] >= 0:
            row = self.cursor[0]
            col = self.cursor[1]

            # setup row and column iterators
            row_iterator = self.doc
            for _ in range(row):
                row_iterator = row_iterator.next

            col_iterator = row_iterator.data
            for _ in range(col):
                if col_iterator.next is not None:
                    col_iterator = col_iterator.next

            # flag to signal if at beginning of line
            beg_of_line = False

            # check if at beginning of line
            if col_iterator.prev == row_iterator:
                beg_of_line = True

            # adjust cursor position if at beginning of line
            if beg_of_line:
                # check if previous row exists and it is not empty
                if row_iterator.prev is not None and row_iterator.prev.data is not None:
                    row_iterator = row_iterator.prev
                    col_iterator = row_iterator.data

                    # get to the last column in line
                    col_counter = 0
                    while col_iterator.next is not None:
                        col_iterator = col_iterator.next
                        col_counter += 1

                    self.cursor[0] = row - 1
                    self.cursor[1] = col_counter
            
            # adjust cursor position if not at beginning of line
            else:
                self.cursor[1] = col - 1

        state = [copy.deepcopy(self.doc), copy.deepcopy(self.cursor)]
        self.stack.push(state)
        
#======================

#======================
    def home(self):
        '''
        Moves the cursor to the start of the current line
 
        Parameters:
            None
        
        Return value:
            None
        '''
        
        state = [copy.deepcopy(self.doc), copy.deepcopy(self.cursor)]
        self.stack.push(state)

        if self.cursor[0] >= 0 and self.cursor[1] >= 0:
            self.cursor[1] = 0

        state = [copy.deepcopy(self.doc), copy.deepcopy(self.cursor)]
        self.stack.push(state)

#======================

#======================
    def end(self):
        '''
        Moves the cursor to the end of the current line
 
        Parameters:
            None
        
        Return value:
            None
        '''
        
        if self.cursor[0] >= 0 and self.cursor[1] >= 0:
            # get to the line cursor is pointing to
            row = self.cursor[0]
            row_iterator = self.doc
            for _ in range(row):
                row_iterator = row_iterator.next

            # find number of columns in line
            col_iterator = row_iterator.data
            col_counter = 0
            while col_iterator.next is not None:
                col_iterator = col_iterator.next
                col_counter += 1

            # move cursor to last column in line
            self.cursor[1] = col_counter

        state = [copy.deepcopy(self.doc), copy.deepcopy(self.cursor)]
        self.stack.push(state)

#======================

#======================
    def insert(self, string):
        '''
        Inserts the given string immediately after the cursor
 
        Parameters:
            a string
        
        Return value:
            None
        '''

        # condition to make sure same values of sheet are not pushed to stack
        if len(self.stack) == 0 or (self.cursor[0] != self.stack.top()[1][0] and self.cursor[1] != self.stack.top()[1][1]):
        # push state to stack for undo and redo operations
            state = [copy.deepcopy(self.doc), copy.deepcopy(self.cursor)]
            self.stack.push(state)
        
        # make string into a list to get individual characters
        string = list(string)
        new_columns = len(string)
        last_index = len(string) - 1

        # move to the node cursor is pointing to
        if self.cursor[0] >= 0 and self.cursor[1] >= 0:
            row = self.cursor[0]
            col = self.cursor[1]

            row_iterator = self.doc
            for _ in range(row):
                row_iterator = row_iterator.next

            col_iterator = row_iterator.data
            for _ in range(col):
                col_iterator = col_iterator.next

        # if cursor is invalid i.e. no nodes exist
        if self.cursor[0] == -1:
            self.doc.data = Node(' ', self.doc)
            col_iterator = self.doc.data
            
            # insert string
            for index, character in enumerate(string):
                col_iterator.data = character
                if index != last_index:
                    col_iterator.next = Node(' ', col_iterator)
                    col_iterator = col_iterator.next

            # set cursor to current position
            self.cursor[0] = 0
            self.cursor[1] = new_columns - 1

        # if nodes dont exist, create them and insert characters
        elif col_iterator.next is None:
            for index, character in enumerate(string):
                col_iterator.data = character
                if index != last_index:
                    col_iterator.next = Node(' ', col_iterator)
                    col_iterator = col_iterator.next

        else:
            row = self.cursor[0]
            col = self.cursor[1]

            # get to the node cursor is pointing to
            row_iterator = self.doc
            for _ in range(row):
                row_iterator = row_iterator.next

            col_iterator = row_iterator.data
            for _ in range(col + 1):
                # make sure a node exists at next position
                if col_iterator.next is None:
                    col_iterator.next = Node(' ', col_iterator)
                col_iterator = col_iterator.next
            
            # insert string
            for index, character in enumerate(string):
                col_iterator.data = character

                if index != last_index and col_iterator.next is None:
                    col_iterator.next = Node(' ', col_iterator)
                
                col_iterator = col_iterator.next

            # set cursor to current position
            self.cursor[1] = col + new_columns

        state = [copy.deepcopy(self.doc), copy.deepcopy(self.cursor)]
        self.stack.push(state)

#======================

#======================
    def delete(self, num):
        '''
        Deletes specified number of characters from the cursor position
 
        Parameters:
            integer number of characters to delete
        
        Return value:
            None
        '''

        # condition to make sure same values of sheet are not pushed to stack
        if len(self.stack) == 0:
        # push state to stack for undo and redo operations
            state = [copy.deepcopy(self.doc), copy.deepcopy(self.cursor)]
            self.stack.push(state)
        
        # check if number is positive and non-zero
        if num > 0:
            if self.cursor[0] >= 0 and self.cursor[1] >= 0:
                row = self.cursor[0]
                col = self.cursor[1]

                # get to the nodes cursor is pointing to
                row_iterator = self.doc
                for _ in range(row):
                    row_iterator = row_iterator.next

                col_iterator = row_iterator.data
                for _ in range(col):
                    col_iterator = col_iterator.next

                # check how many characters are in the line
                col_counter = 0
                temp = row_iterator.data
                while temp is not None:
                    col_counter += 1
                    temp = temp.next

                # if entire line is deleted point cursor to first character of next line
                if self.cursor[1] == 0 and num >= col_counter:
                    col_iterator = row_iterator.data
                    col_iterator.prev = None
                    row_iterator.data = None

                    # create the next row if it doesn't exist
                    if row_iterator.next is None:
                        row_iterator.next = Node(None, row_iterator)
                        row_iterator = row_iterator.next
                    # create the first character in next line if it doesn't exist
                    if row_iterator.data is None:
                        row_iterator.data = Node(' ', row_iterator)

                    self.cursor[0] = row + 1
                    self.cursor[1] = 0

                # check if deletion number is greater than character in line
                # if yes then point to the first character after deletion of all other nodes
                elif num > col_counter:
                    first_col = row_iterator.data
                    col_iterator = first_col.next
                    first_col.next = None
                    for _ in range(col_counter - 1):
                        temp = col_iterator
                        col_iterator = col_iterator.next
                        temp.prev = None
                        temp.next = None

                    self.cursor[1] = 0
                    col_counter = 1

                # deleting exact number of characters as input
                else:
                    for i in range(num):
                        temp = col_iterator
                        col_iterator = col_iterator.next
                        prev = temp.prev
                        next = temp.next
                        if temp.next is not None:
                            temp.next.prev = prev
                        if prev is row_iterator and i == (num - 1):
                            row_iterator.data = temp.next
                            temp.next = None
                            temp.prev = None
                            col_counter -= 1
                        elif prev is row_iterator:
                            row_iterator.data = temp
                            temp.next = None
                            temp.prev = None
                            col_counter -= 1
                        else:
                            temp.prev.next = next
                            temp.next = None
                            temp.prev = None
                            col_counter -= 1

        state = [copy.deepcopy(self.doc), copy.deepcopy(self.cursor)]
        self.stack.push(state)

#======================

#======================
    def countCharacters(self):
        '''
        Counts the number of characters in the text editor
 
        Parameters:
            None
        
        Return value:
            total number of characters in the document, basically
               the total number of col_iterator nodes in the document.
        '''
        
        pink_nodes = 0

        row_iterator = self.doc
        while row_iterator is not None:
            if row_iterator.data is not None:
                col_iterator = row_iterator.data
                while col_iterator is not None:
                    col_iterator = col_iterator.next
                    pink_nodes += 1

            row_iterator = row_iterator.next
        
        return pink_nodes

#======================

#======================
    def countLines(self):
        '''
        Count total of non-empty lines in the document.
 
        Parameters:
            None
        
        Return value:
            integer number of non-empty lines in the document
        '''
        
        row_iterator = self.doc
        non_empty_lines = 0

        while row_iterator is not None:
            if row_iterator.data is not None:
                non_empty_lines += 1

            row_iterator = row_iterator.next

        return non_empty_lines

#======================


#======================
    def printDoc(self):
        '''
        Prints the entire document on the screen.
        '''
        
        row = 0
        col = 0
        row_iterator = self.doc

        while row_iterator is not None:
            # printing for empty lines
            if row_iterator.data is None:
                print()
            else:
                # printing for non-empty lines
                col_iterator = row_iterator.data
                while col_iterator is not None:
                    # check to maintain lines using 'end'
                    if col_iterator.next is None:
                        # check to print cursor position
                        if row == self.cursor[0] and col == self.cursor[1]:
                            print("|", end='')
                        print(col_iterator.data)
                    else:
                        if row == self.cursor[0] and col == self.cursor[1]:
                            print("|", end='')
                        print(col_iterator.data, end='')
                    
                    col_iterator = col_iterator.next
                    col += 1

            row_iterator = row_iterator.next
            row += 1
            col = 0

#======================

            
#======================
#======================
#    BONUS
#======================
    def undo(self):
        '''
        Undo the previous action by user.
 
        Parameters:
            None
        
        Return value:
            None 

        '''
        
        if self.stack.top() is not None:
            # move state to redo stack
            self.redo_stack.push(self.stack.pop())
            self.doc = self.stack.top()[0]
            self.cursor = self.stack.top()[1]
        else:
            print('No action to undo')

#----------------------

    def redo(self):
        '''
        Redos the previous action undone by user.
 
        Parameters:
            None
        
        Return value:
            None 

        '''
        
        if self.redo_stack.top() is not None:
            self.stack.push(self.redo_stack.pop())
            self.doc = self.stack.top()[0]
            self.cursor = self.stack.top()[1]
        else:
            print('No action to redo')

#----------------------

    def save(self, fileName):
        '''
        Saves the spreadsheet to a file with name given as Parameter
 
        Parameters:
            fileName
        
        Return value:
            None 

        '''
        
        text_file = open(fileName + '.txt', 'w')

        row_iterator = self.doc
        
        while row_iterator is not None:
            if row_iterator.data is None:
                print('', file=text_file)
            else:
                col_iterator = row_iterator.data
                while col_iterator is not None:
                    print(col_iterator.data, end='', file=text_file)
                    col_iterator = col_iterator.next

            row_iterator = row_iterator.next

        text_file.close()

#----------------------

    def load(self, fileName):
        '''
        Loads the spreadsheet from a file with name given as Parameter
 
        Parameters:
            fileName
        
        Return value:
            None 

        '''
        
        text_file = open(fileName + '.txt', 'r')
        row_iterator = self.doc

        # make it a list so an extra line doesn't print in the end
        line_list = text_file.read().split('\n') 
        line_length = len(line_list) - 1

        for line_num,line in enumerate(line_list):
            line = line.rstrip('\n')

            # check if empty line or not
            if line.strip() != '':
                line = list(line)
                last_index = len(line) - 2

                col_iterator = Node(line[0], row_iterator)
                row_iterator.data = col_iterator
                col_iterator.next = Node(' ', col_iterator)
                col_iterator = col_iterator.next
                for index, character in enumerate(line[1::]):
                    col_iterator.data = character
                    if index != last_index:
                        col_iterator.next = Node(' ', col_iterator)
                        col_iterator = col_iterator.next
            
            if line_num != line_length:
                row_iterator.next = Node(None, row_iterator)
            row_iterator = row_iterator.next

        text_file.close()
        
        # set cursor to the first position
        self.cursor[0] = 0
        self.cursor[1] = 0
            
#----------------------

    def find(self, substr):
        '''
        Finds a given substring within the entire document. If no such substring
          is found then return None.
 
        Parameters:
            substring to look for
        
        Return value:
            - reference to the first node of the substring found
            - None if substring is not found
        '''
        
        reference = None
        queue = list(substr)

        row = 0
        col = 0

        substring_check = []
        row_iterator = self.doc
        while row_iterator is not None:
            if row_iterator.data is not None:
                col_iterator = row_iterator.data

                while col_iterator is not None:
                    if col_iterator.data in queue:
                        substring_check.append(col_iterator.data)

                    substring_check = ''.join(substring_check)
                    if substr in substring_check:
                        if col == 0:
                            reference = (f'\nFound at:\nrow: {row}, column: {col + 1}')
                        else:
                            reference = (f'\nFound at:\nrow: {row}, column: {col - len(substr) + 1}')

                        return reference

                    substring_check = list(substring_check)
                    col_iterator = col_iterator.next
                    col += 1

            row_iterator = row_iterator.next
            row += 1
            col = 0

        return reference  
                
#======================


#======================
#======================
#
#    DRIVER FUNCTION
#
#======================

def main():
    # -----------------------------
    # Implement your own logic here:
    # -----------------------------
    editor = TextEditor()
    
    # menu for entering commands
    # quits program if "quit" is entered
    # case-sensitive so input should be same as functions
    print("Welcome to DS Text Editor\nEnter Command:")
    command = input()

    valid_cursor = False

    while command != "quit":
        command_list = command.split(' ')
        if command_list[0] == "goto":
            editor.goto(int(command_list[1]), int(command_list[2]))
            valid_cursor = True
        elif command_list[0] == "forward" and valid_cursor:
            editor.forward()
        elif command_list[0] == "back" and valid_cursor:
            editor.back()
        elif command_list[0] == "home" and valid_cursor:
            editor.home()
        elif command_list[0] == "end" and valid_cursor:
            editor.end()
        elif command_list[0] == "insert":
            editor.insert(command[7::])
            valid_cursor = True
        elif command_list[0] == "delete" and valid_cursor:
            editor.delete(int(command_list[1]))
        elif command_list[0] == "countCharacters" and valid_cursor:
            print(editor.countCharacters())
        elif command_list[0] == "countLines" and valid_cursor:
            print(editor.countLines())
        elif command_list[0] == "printDoc" and valid_cursor:
            editor.printDoc()
        elif command_list[0] == "save" and valid_cursor:
            editor.save(command_list[1])
        elif command_list[0] == "load":
            editor.load(command_list[1])
            valid_cursor = True
        elif command_list[0] == "undo" and valid_cursor:
            editor.undo()
        elif command_list[0] == "redo" and valid_cursor:
            editor.redo()
        elif command_list[0] == "find" and valid_cursor:
            print(editor.find(command_list[1]))
        else:
            print("command is invalid or cursor must be set using goto first")
        command = input()
    

if __name__ == '__main__':
    main()
    
#======================


