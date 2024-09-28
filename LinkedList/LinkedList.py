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

    # simple prepend function for my LL class
    def prepend(self, value):
        new_node = Node(value)
        
        # simple edge case: empty list
        if self.length == 0:
            self.tail = new_node
            self.head = new_node
        else:
            # make the next value equal to the beginning of the list aka the head
            new_node.next = self.head
            # now we reassign the head value
            self.head = new_node
        
        self.length += 1
        
        return True

    # This is the pop_first function for my LL class:
    def pop_first(self):
        # Simple edge case
        if self.length == 0:
            return None
        # assign a temp variable to head
        temp = self.head
        # head is now equal to the subsequent node
        self.head = self.head.next
        # now we disconnect the temp node from the LL
        temp.next = None
        # lastly we decrement by 1
        self.length -= 1
        # There could be a situation where we have 1 node in the LL, and after we decrement it is 0
        if self.length == 0:
            self.tail = None
        return temp
    
    # This is the get function for my LL
    def get(self, index):
        # taking care of simple edge cases:
        # 1: if index is negative
        # 2: if index is outside of range
        if index < 0 or index >= self.length:
            return None
        
        # temp variable
        temp = self.head
        # the reason we do not have a variable for our counter is because we do not need it inside the for loop
        for _ in range(index):
           temp = temp.next 
        
        return temp
    
    # this is the set method for my LL class
    # Note: cannot directly say set(...) because it is a key word within python
    def set_value(self, index, value):
        # grabbing the index we need
        temp = self.get(index)
        
        if temp is not None:
            temp.value = value
            return True
        
        return False

        

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

print("Now testing the prepend function by adding Node 9 to the beginning of the list.")
my_linked_list.prepend(9)

print("To prove it worked, we can now use the print function to show the new LL:")
my_linked_list.print_list()

print("Now testing the pop first function by removing Node 9 at the beginning of the list.")
my_linked_list.pop_first()

print("To prove it worked, we can now use the print function to show the new LL:")
my_linked_list.print_list()

print("Now testing the get function by grabbing Node 4.")
print(my_linked_list.get(0))

print("Now I will add more nodes to my LL.")
my_linked_list.append(5)
my_linked_list.append(6)
my_linked_list.append(7)
my_linked_list.append(8)
my_linked_list.prepend(3)
my_linked_list.prepend(2)
my_linked_list.prepend(1)

print("This is the new LL:")
my_linked_list.print_list()

print("Now testing the get function by changing Node 6 to Node 9")
my_linked_list.set_value(5, 9)

print("To prove it worked, we can now use the print function to show the new LL:")
my_linked_list.print_list()