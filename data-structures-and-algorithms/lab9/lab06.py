#=============================================
#=============================================
# Name   : Daim Bin Khalid
# Roll no: 251686775
# Section: C
# Date   : 06/12/2022
#=============================================

#=============================================
#  TASK L01: Node class creation
#---------------------------------------------
class Node:
    def __init__(self, data, prev=None, next=None):
        #==================
        # Insert code here:
        #------------------
        self.data = data
        self.prev = prev
        self.next = next
 
        #==================

#=============================================        

    
#=============================================
#  TASK L02: 
#---------------------------------------------
def TaskL02():

    head = Node(1)            # DO NOT MODIFY THIS LINE

    #==================
    # Insert code here:
    #------------------
    one = Node(2)
    head.next = one
    one.prev = head

    two = Node(3)
    one.next = two
    two.prev = one

    three = Node(4)
    two.next = three
    three.prev = two    
    
    #------------------
    
    return head               # DO NOT MODIFY THIS LINE
    
#=============================================


#=============================================
#  TASK L03: 
#---------------------------------------------
def TaskL03(head, data):
    
    node = None            # DO NOT MODIFY THIS LINE

    #==================
    # Insert code here:
    #------------------
    temp = head
    while temp != None:
        if temp.data == data:
            node = temp
            
        temp = temp.next
   
    #==================

    return node               # DO NOT MODIFY THIS LINE
    
#=============================================


#=============================================
#  TASK L04: 
#---------------------------------------------
def TaskL04(L1, L2):
    #==================
    # Insert code here:
    #------------------
    first_iterator = L1
    while first_iterator.next != None:
        first_iterator = first_iterator.next

    first_iterator.next = L2
    first_iterator.next.prev = first_iterator

    #==================
    return L1               # DO NOT MODIFY THIS LINE

    
#=============================================


#=============================================
#  TASK L05: 
#---------------------------------------------
def TaskL05():
    
    head = None               # DO NOT MODIFY THIS LINE
    
    #==================
    # Insert code here:
    #------------------
    head = Node(None)
    r2 = Node(None)
    head.next = r2
    r2.prev = head

    #==================
    return head               # DO NOT MODIFY THIS LINE

    
#=============================================



#=============================================
#  TASK L06: 
#---------------------------------------------
def TaskL06():
    
    head = None               # DO NOT MODIFY THIS LINE
    
    #==================
    # Insert code here:
    #------------------
    head = TaskL05()

    # First pink row:
    c1 = Node(1)
    c2 = Node(2)
    c1.next = c2
    c2.prev = c1

    # c1 acts as the head of the first pink row
    head.data = c1  #NOTE: we're putting the row's head in data
    c1.prev = head

    # Second pink row:
    c3 = Node(3)

    r2 = head.next
    # c3 acts as the head of the second pink row
    r2.data = c3 #NOTE: we're putting the row's head in data
    c3.prev = r2

    #==================
    return head               # DO NOT MODIFY THIS LINE

#=============================================




#=============================================
#  TASK L07: 
#---------------------------------------------
def TaskL07():
    
    head = None               # DO NOT MODIFY THIS LINE
    
    #==================
    # Insert code here:
    #------------------

    # green list
    green1 = Node(None)
    head = green1
    green2 = Node(None, green1)
    green1.next = green2
    green3 = Node(None, green2)
    green2.next = green3
    green4 = Node(None, green3)
    green3.next = green4

    # first red list
    red1 = Node(1, head)
    red2 = Node(2, red1)
    red1.next = red2
    green1.data = red1  # linking the red list with green1.data

    # second red list
    sec_row1 = Node(4, green3)
    sec_row2 = Node(5, sec_row1)
    sec_row1.next = sec_row2
    sec_row3 = Node(6, sec_row2)
    sec_row2.next = sec_row3
    green3.data = sec_row1 # linking second red list with green3.data

    # third red list
    third_row1 = Node(3, green4)
    green4.data = third_row1 # linking third red list with green4.data

    #==================

    return head               # DO NOT MODIFY THIS LINE

#=============================================




#=============================================
#  TASK L08: 
#---------------------------------------------
def TaskL08(head):    
    #==================
    # Insert code here:
    #------------------
    counter = 0
    temp = head
    while temp != None:
        if temp.data != None:
            counter += 1

        temp = temp.next

    return counter
    
    #==================

#=============================================




#=============================================
#  TASK L09: 
#---------------------------------------------
def TaskL09(head):    
    #==================
    # Insert code here:
    #------------------
    counter = 0
    temp = head
    nested_iterator = None
    while temp != None:
        if temp.data != None:
            nested_iterator = temp.data
            while nested_iterator != None:
                counter += 1
                nested_iterator = nested_iterator.next

        temp = temp.next
    
    return counter
    #==================

#=============================================



#=============================================
#  TASK L10: 
#---------------------------------------------
def TaskL10(head, node, currentRow):
    '''
    Parameters:
    -----------
        head - the root reference of the entire nested structure
        node - the random node in a row to begin with
        currentRow - Reference of the GREEN node that contains this row
    '''

    rowHead = None              # DO NOT MODIFY THIS LINE

    #==================
    # Insert code here:
    #------------------
    pass
    #==================

    return rowHead              # DO NOT MODIFY THIS LINE

#=============================================

