# ===================================
# ===================================
# Name   :   Daim Bin Khalid
# Roll no:    251686775
# Section:   COMP 200 - C
# Date   :    15/11/2022
# ===================================
# ===================================

import copy


class Spreadsheet:
    def __init__(self):
        '''
        Predefined member variables. 
        
        WARNING:DO NOT MODIFY THE FOLLOWING VARIABLES
        '''
        self.sheet = None  # 2D array of values
        self.rows = 0
        self.cols = 0
        self.cursor = [0, 0]  # cursor's current position
        self.selction = [None, None, None, None]

        # ======================
        # Insert your Member
        #   variables here (if any):
        self.stack = []
        self.redo_stack = []

        # ======================

    # ======================
    def CreateSheet(self, rows, cols):
        """
        Creates a new 2 dimensional array assigned
          to the self.sheet member variable.
        Initialize the 2D array with 'None' type.

        Parameters:
            rows --> total number of rows in this spreadsheet
            cols --> total number of cols in this spreadsheet

        Return value:
            None
        """

        # modify rows and cols according to input of spreadsheet size
        self.rows = rows
        self.cols = cols
        # create lists within a list using nested loop to make 2D array
        self.sheet = [[None for i in range(self.cols)] for j in range(self.rows)]

    # ======================

    # ======================
    def Goto(self, row, col):
        """
        Moves the cursor to the location indicated by the
          row and col parameters

        Parameters:
            row --> row number to move to
            col --> column number to move to

        Return value:
            None
        """

        # change cursor values to use it as a locator within spreadsheet
        self.cursor = [row, col]

    # ======================

    # ======================
    def Insert(self, val):
        """
        Inserts value at the position indicated by the cursor.

        Parameters:
            val --> value to be inserted at the cursor location

        Return value:
            None
        """

        # condition to make sure same values of sheet are not pushed to stack
        if len(self.stack) == 0 or self.sheet != self.stack[-1]:
            # insert deepcopy of sheet into stack before any insertion
            self.stack.append(copy.deepcopy(self.sheet))
            # accessing row as first index and column as second index to assign value entered by user
            self.sheet[self.cursor[0]][self.cursor[1]] = val
            # insert the version of sheet to stack after insertion
            self.stack.append(copy.deepcopy(self.sheet))
        else:
            self.sheet[self.cursor[0]][self.cursor[1]] = val
            self.stack.append(copy.deepcopy(self.sheet))

    # ======================

    # ======================
    def Delete(self):
        """
        Deletes a value from the position indicated by the cursor.

        Parameters:
            None

        Return value:
            None
        """

        # condition to make sure same values of sheet are not pushed to stack
        if len(self.stack) == 0 or self.sheet != self.stack[-1]:
            # insert the sheet into stack before deletion
            self.stack.append(copy.deepcopy(self.sheet))
            # accessing row as first index and column as second index to assign value of None
            self.sheet[self.cursor[0]][self.cursor[1]] = 0
            # insert the version of sheet to stack after deletion
            self.stack.append(copy.deepcopy(self.sheet))
        else:
            self.sheet[self.cursor[0]][self.cursor[1]] = 0
            self.stack.append(copy.deepcopy(self.sheet))

    # ======================

    # ======================
    def ReadVal(self):
        """
        Prints the value from the position indicated by the cursor.

        Parameters:
            None

        Return value:
            value stored at the cursor location

        """

        print(self.sheet[self.cursor[0]][self.cursor[1]])

    # ======================

    # ======================
    def Select(self, row, col):
        """
        Selects values between the position indicated in arguments with row and col and the position indicated by the cursor

        Parameters:
            row --> Row number to be selected
            col --> Column number to be selected

        Return value:
            None
        """

        # modify the value of selection by [starting row, starting column, ending row, ending column] of selection
        self.selction = [self.cursor[0], self.cursor[1], row, col]

    # ======================

    # ======================
    def GetSelection(self):
        """
        Returns a tuple with current selection coordinates
        Parameters:
            None

        Return value:
            Returns a tuple with row and column of the selection:
                position 1 of the tuple indicates the stating row of the selection
                position 2 of the tuple indicates the stating col of the selection
                position 3 of the tuple indicates the ending row of the selection
                position 4 of the tuple indicates the ending col of the selection

            Example: (1,1,3,4)
        """
        # tuple will be returned of selected points
        return self.selction[0], self.selction[1], self.selction[2], self.selction[3]

    # ======================

    # ======================
    def Sum(self, row, col):
        """
        Stores the sum of the values in the current selction at the position indicated in arguments
        Parameters:
            row --> Row number to store the sum
            col --> Column number to store the sum

        Return value:
            None
        """

        # condition to make sure same values of sheet are not pushed to stack
        if len(self.stack) == 0 or self.sheet != self.stack[-1]:
            # insert the sheet into stack before taking sum
            self.stack.append(copy.deepcopy(self.sheet))

        # create a list of indexes of the columns that are under selection
        columns = [i for i in range(self.selction[1], self.selction[3] + 1)]

        total = 0
        # iterating through the sliced list of rows that are under selection
        for r_index, val in enumerate(self.sheet[self.selction[0]: self.selction[2] + 1], self.selction[0]):
            # iteration through each column element. a check makes sure that the element used is under selection
            for c_index, c in enumerate(val):
                if c_index in columns:
                    if self.sheet[r_index][c_index] is not None:
                        total += self.sheet[r_index][c_index]

        # point cursor at the cell to store value in
        self.cursor = [row, col]
        self.sheet[self.cursor[0]][self.cursor[1]] = total

        # insert the version of sheet to stack after taking sum
        self.stack.append(copy.deepcopy(self.sheet))

    # ======================

    # ======================
    def Mul(self, row, col):
        """
        Stores the product of the values in the current selection at the position indicated in arguments
        Parameters:
            row --> Row number to store the product
            col --> Column number to store the product

        Return value:
            None
        """

        # condition to make sure same values of sheet are not pushed to stack
        if len(self.stack) == 0 or self.sheet != self.stack[-1]:
            # insert the sheet into stack before taking multiplication
            self.stack.append(copy.deepcopy(self.sheet))

        # create a list of indexes of the columns that are under selection
        columns = [i for i in range(self.selction[1], self.selction[3] + 1)]

        total = 1
        # iterating through the sliced list of rows that are under selection
        for r_index, val in enumerate(self.sheet[self.selction[0]: self.selction[2] + 1], self.selction[0]):
            # iteration through each column element. a check makes sure that the element used is under selection
            for c_index, c in enumerate(val):
                if c_index in columns:
                    if self.sheet[r_index][c_index] is not None:
                        total *= self.sheet[r_index][c_index]

        # point cursor at the cell to store value in
        self.cursor = [row, col]
        self.sheet[self.cursor[0]][self.cursor[1]] = total

        # insert the version of sheet to stack after multiplication
        self.stack.append(copy.deepcopy(self.sheet))

    # ======================

    # ======================
    def Avg(self, row, col):
        """
        Stores the average of the values in the current selection at the position indicated in arguments
        Parameters:
            row --> Row number to store the average
            col --> Column number to store the average

        Return value:
            None
        """

        # condition to make sure same values of sheet are not pushed to stack
        if len(self.stack) == 0 or self.sheet != self.stack[-1]:
            # insert the sheet into stack before taking average
            self.stack.append(copy.deepcopy(self.sheet))

        # create a list of indexes of the columns that are under selection
        columns = [i for i in range(self.selction[1], self.selction[3] + 1)]

        total = 0
        number_of_elements = 0
        # iterating through the sliced list of rows that are under selection
        for r_index, val in enumerate(self.sheet[self.selction[0]: self.selction[2] + 1], self.selction[0]):
            # iteration through each column element. a check makes sure that the element used is under selection
            for c_index, c in enumerate(val):
                if c_index in columns:
                    if self.sheet[r_index][c_index] is not None:
                        total += self.sheet[r_index][c_index]
                        number_of_elements += 1

        # point cursor at the cell to store value in
        self.cursor = [row, col]
        self.sheet[self.cursor[0]][self.cursor[1]] = total

        # take average
        average = total / number_of_elements
        # point cursor at the cell to store value in
        self.cursor = [row, col]
        self.sheet[self.cursor[0]][self.cursor[1]] = average

        # insert the sheet into stack after taking average
        self.stack.append(copy.deepcopy(self.sheet))

    # ======================

    # ======================
    def Max(self, row, col):
        """
        Stores the maximum of the values in the current selection at the position indicated in arguments
        Parameters:
            row --> Row number to store the maximum
            col --> Column number to store the maximum

        Return value:
            None
        """

        # condition to make sure same values of sheet are not pushed to stack
        if len(self.stack) == 0 or self.sheet != self.stack[-1]:
            # insert the sheet into stack before finding max value
            self.stack.append(copy.deepcopy(self.sheet))

        # create a list of indexes of the columns that are under selection
        columns = [i for i in range(self.selction[1], self.selction[3] + 1)]

        total = []
        # iterating through the sliced list of rows that are under selection
        for r_index, val in enumerate(self.sheet[self.selction[0]: self.selction[2] + 1], self.selction[0]):
            # iteration through each column element. a check makes sure that the element used is under selection
            for c_index, c in enumerate(val):
                if c_index in columns:
                    if self.sheet[r_index][c_index] is not None:
                        total.append(self.sheet[r_index][c_index])

        # point cursor at the cell to store value in and use max() function
        self.cursor = [row, col]
        self.sheet[self.cursor[0]][self.cursor[1]] = max(total)

        # insert the sheet into stack after finding max value
        self.stack.append(copy.deepcopy(self.sheet))

    # ======================

    # ======================
    def PrintSheet(self):
        """
        Prints the sheet in a human readable from
        Parameters:
            None
        Return value:
            None

        Note: This is an example output your values will differ
        PrintSheet()
        row/col:    0   1   2   3   4
            0
            1
            2           10
            3                   12
            4
        """

        row_num = len(max(self.sheet, key=len))

        # columns
        print('  ', end='')
        print(*range(row_num), sep='\t\t')

        # rows
        for index, val in enumerate(self.sheet):
            print(index, end=' ')
            print(*val, sep='\t\t')

    # ======================

    # ======================
    # ======================
    #    BONUS
    # ======================

    def Undo(self):
        # Undoes the previous action by user.

        # cancel the last action and move sheet to the backup stack
        self.redo_stack.append(self.stack.pop())
        self.sheet = self.stack[-1]

    # ----------------------

    def Redo(self):
        # Redoes the previous action undone by user.

        # transfer the previous action from backup stack to main stack
        self.stack.append(self.redo_stack.pop())
        self.sheet = self.stack[-1]

    # ----------------------

    def Save(self, fileName):
        # Saves the spreadsheet to a file with name given as Parameter

        # navigate through array to check and write each element to file
        save_file = open(fileName + '.txt', 'a+')
        for row_index, row in enumerate(self.sheet):
            for col_index, col in enumerate(row):
                if col_index == len(row) - 1:
                    if self.sheet[row_index][col_index] is None:
                        print("None", file=save_file)
                    else:
                        print(self.sheet[row_index][col_index], file=save_file)

                else:
                    if self.sheet[row_index][col_index] is None:
                        print("None", end=",", file=save_file)
                    else:
                        print(self.sheet[row_index][col_index], end=",", file=save_file)
        save_file.close()

    # ----------------------

    def Load(self, fileName):
        # Loads the spreadsheet from a file with name given as Parameter

        # initialise self.sheet as a list
        self.sheet = []

        array_file = open(fileName + '.txt', 'r')
        for line in array_file:
            line = line.strip("\n")
            line_array = line.split(',')
            # assign a list with indexes equal to the ones in line_array
            row = [0] * len(line_array)
            for element_index, element in enumerate(line_array):
                # format numbers in float and empty spaces as None
                if element == 'None':
                    row[element_index] = None
                else:
                    row[element_index] = float(element)

            self.sheet.append(row)
        array_file.close()

        # assign values to rows and columns of the spreadsheet
        self.rows = len(self.sheet)
        self.cols = len(self.sheet[0])


# ======================


# ======================
# ======================
#
#    DRIVER FUNCTION
#
# ======================

def main():
    # -----------------------------
    # Implement your own logic here:
    # -----------------------------
    sheet = Spreadsheet()
    sheet_created = False

    # menu for entering commands
    # quits program if "Quit" is entered
    # case-sensitive so input should be same as functions
    print("Welcome to DS SpreadSheet Program\nEnter Command:")

    command = input()
    while command != "Quit":
        command_list = command.split(' ')
        if command_list[0] == "CreateSheet":
            sheet.CreateSheet(int(command_list[1]), int(command_list[2]))
            sheet_created = True
        elif command_list[0] == "Goto" and sheet_created is True:
            sheet.Goto(int(command_list[1]), int(command_list[2]))
        elif command_list[0] == "Insert" and sheet_created is True:
            sheet.Insert(int(command_list[1]))
        elif command_list[0] == "Delete" and sheet_created is True:
            sheet.Delete()
        elif command_list[0] == "ReadVal" and sheet_created is True:
            sheet.ReadVal()
        elif command_list[0] == "Select" and sheet_created is True:
            sheet.Select(int(command_list[1]), int(command_list[2]))
        elif command_list[0] == "GetSelection" and sheet_created is True:
            print(sheet.GetSelection())
        elif command_list[0] == "Sum" and sheet_created is True:
            sheet.Sum(int(command_list[1]), int(command_list[2]))
        elif command_list[0] == "Mul" and sheet_created is True:
            sheet.Mul(int(command_list[1]), int(command_list[2]))
        elif command_list[0] == "Avg" and sheet_created is True:
            sheet.Avg(int(command_list[1]), int(command_list[2]))
        elif command_list[0] == "Max" and sheet_created is True:
            sheet.Max(int(command_list[1]), int(command_list[2]))
        elif command_list[0] == "PrintSheet" and sheet_created is True:
            sheet.PrintSheet()
        elif command_list[0] == "Save":
            sheet.Save(command_list[1])
        elif command_list[0] == "Load":
            sheet.Load(command_list[1])
            sheet_created = True
        elif command_list[0] == "Undo" and sheet_created is True:
            sheet.Undo()
        elif command_list[0] == "Redo" and sheet_created is True:
            sheet.Redo()
        else:
            print("Command is invalid OR No sheet has been created")
        command = input()


if __name__ == '__main__':
    main()

# ======================
