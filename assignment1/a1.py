"""ASSIGNEMNT 1 :
IMPLEMENTATION IS USING LINKED LISTS"""

"""below is the Node class which creates a list or a array type named data and assigh a next to it
data stored the value assigned to it and next points to the next link in the list """
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
"""this is the implementation of stack using Linked lists. Here the LIFO policy is used as follows
    The element is pushed and removed from the front of thelinked list. 
    That is , the head element is the top element of the Stack.
    This stack uses only the required method to reduce the space complexity of the progremme. for example length of stack, printig stack, is_empty metond... """
class Stack:
    def __init__(self):
        self.head =None
        self.size = 0
    # this method is used to add data to the stack.
    def push(self,data):
        if self.head == None: # if there is no data added to the Stack, then simple data is added to the stack by envoking the Node class
            self.head=Node(data) # no further links to manage
        else: # if there is data prsent in the stack 
            new_node = Node(data)  # create a new node element 
            new_node.next = self.head  # make the link between this new node and thestack 
            self.head = new_node # assign this new node the head position of the stack
        self.size+=1
    # Returns the top element of the stack 
    def top(self):
        return self.head.data

	# Remove the top element of the stack
    def pop(self):
        old = self.head  # temporarily stores the head value of the stack 
        self.head = self.head.next  # assigh the head position to the next element(after head) of the stack 
        old.next = None # old now has a link with None
        self.size -=1
        return old.data# return the old value 
	
"""this function takes the input as string and gives the output as x,y,z,distance moves"""	
def findPositionandDistance(p):
    pos_val = Stack()  # this initialise the number as encountered in the string
    number_stack = Stack()  # this is a stack which will store then values of numbers as encountered by the loop. Bascially the number int his will be the times by which the drone has moved in the specific direction 
    number_stack.push(1) # initially numbe rof times the coordinates will be increased will be one   
    x_coor = 0 # initial value of x coordinate
    y_coor = 0 # initial value of y coordinate 
    z_coor = 0 # initial value of z coordinate
    dist_move = 0 # initial distance moved 
    i = 0 # initialization for while loop
    while i < len(p):
        helpr = number_stack.top() #top value in the stack
        # if p[i] is + or - or any of the coordinate
        if p[i] == "+" : # if it is increase in coordinate 
                if p[i+1]=="X": # increase in x 
                    x_coor += helpr  # number stack stores how many times the increase is happening 
                    dist_move+= helpr  # updation of distance value 
                    i+=2 # this will take i to the next of the coordinate i.e after +X
                elif p[i+1] == "Y":  # smae in case of y 
                    y_coor += helpr
                    dist_move+= helpr
                    i+=2
                elif p[i+1] =="Z": # same in case of z 
                    z_coor +=helpr
                    dist_move+=helpr
                    i+=2
        elif p[i] == "-" :  # if it is decrease in the coordinate 
                if p[i+1]=="X":
                        x_coor -= helpr  # + has been replaced by - . rest the logic remains the same 
                        dist_move+=helpr
                        i+=2
                elif p[i+1] == "Y": # smae for y 
                        y_coor -=helpr
                        dist_move+=helpr
                        i+=2
                elif p[i+1] =="Z": # same for z 
                        z_coor -=helpr
                        dist_move+=helpr
                        i+=2
        elif p[i].isdigit()==True:  # if digit is encountered 
            if pos_val.size ==0:
                pos_val.push(i)# number string will store the number encountered 
            i+=1  # increment in i 
        elif p[i] == ')':   # if closed bracket is encountered 
            number_stack.pop()  # remove the last element of the muber stack. because outside the bracket the multiple by which a variable will be strored is the previous value store in the numbr stack 
            i+=1 # increment of x  
            pass
        elif p[i] =='(':  # open bracket is encountered 
            number = p[pos_val.pop():i]  # numbe is not empty # value of h is the new number times the previous number in the number_stack 
            number_stack.push(helpr * int(number)) # append of h in the number stack 
            i+=1 # updation of i
    return [x_coor,y_coor,z_coor,dist_move]
"""time complexity : O(n) as only one iteration is done on the string. The methos in the class are O(1)"""