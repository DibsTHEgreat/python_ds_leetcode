# This file contains my observations and notes about the Data Structure: Linked List

# LL do not have indexes, and is NOT in a contiguous place in memory. As in they are all spread out in memory.

# Keep in mind that a normal list is in a contiguous place in memory, so they are all right next to each other in memory, hence why we can use indexes.

# There is a variable called head which points to the first node in the LL
# There is a variable called tail which points to the last node in the LL
# Each node points to the next one (one-way direction)
# The last node will point to None

# Example:

# Head                            Tail
#   |                               |
#  (1) --> (2) --> (3) --> (4) --> (5) --> None

# Basic Big O Notation for LL:

# When appending onto a LL, the Big O is constant time O(1).

# Step 1: 

# Head                            Tail
#   |                               |
#  (1) --> (2) --> (3) --> (4) --> (5) --> None         (6)-->

# Step 2: 

# Head                                    Tail
#   |                                       |
#  (1) --> (2) --> (3) --> (4) --> (5) --> (6)--> None

# The story changes when we want to remove, mainly because now node 5 has to point to None, not only that tail has to be moved back to node 5
# In order to get to that node, we have to iterate through the LL.

# Even for other operations, if you have to iterate through the LL, it is considered O(n)

# Creating a Helper Class for my LL class:
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
# Now I will create a class for my LL:
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        # attaching head to the new node since it is the first node in the list
        self.head = new_node
        # Since there is only 1 node in the list, head = tail, hence tail is new node also
        self.tail = new_node
        # Only one node in the list
        self.length = 1
    
    # This function will allow me to print my LL, one node at a time
    def print_list(self):
        # assigning a temp variable to head node
        temp = self.head
        
        # while temp is not None, we iterate through the list
        while temp is not None:
            # print the value of each node
            print(temp.value)
            # assign temp the next node
            temp = temp.next
            
    # This is the append function for my LL class
    def append(self, value):
        new_node = Node(value)
        
        # First we tackle a specific edge case for the append function     
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
        # if it is a normal list, all we do is reassign the tail
            self.tail.next = new_node
            self.tail = new_node
            
        # since new node is added, we can add to the length of the LL
        self.length += 1
        
        # only returning true for another method, not really needed for the append function
        return True

    # Pop function for my LL class
    def pop(self):
        # catching simple edge case
        if self.length == 0:
            return None
        
        # now we will create simple helper variables to iterate through the list
        temp = self.head
        pre = self.head
        
        # while temp.next is Not None, we iterate through the list
        while(temp.next):
            # assign pre to temp
            pre = temp
            # now we move temp to next node
            temp = temp.next
        
        # Ideally when the loop finishes, temp points at the node we want to get rid off
        # And pre points at the new last node
        self.tail = pre
        self.tail.next = None
        
        # Minus 1 the LL, since a node has been removed
        self.length -= 1
        
        # we only do this if there was only one node at the beginning of the list
        if self.length == 0:
            self.head = None
            self.tail = None
        
        return temp.value
        
            


print("Using the constructor func:")
my_linked_list = LinkedList(4)

print("The Head of the new LL:")
print(my_linked_list.head.value)

print("Now testing the append function by adding Node 3:")
my_linked_list.append(3)
print("To prove it worked, we can now use the print function to show the new LL:")
my_linked_list.print_list()

print("Now testing the pop function by removing Node 3:")
print(my_linked_list.pop())

print("To prove it worked, we can now use the print function to show the new LL:")
my_linked_list.print_list()