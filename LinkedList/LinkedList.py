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

# Creating a Helper Function for my LL class:
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

print("Using the constructor func:")
my_linked_list = LinkedList(4)

print("The Head of the new LL:")
print(my_linked_list.head.value)
        