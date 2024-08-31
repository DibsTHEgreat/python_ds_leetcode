# Built in HashTable which is dictionary
# Dictionaries are made up of key-value pairs

# For example: { "nails": 1000}
# What we're going to do is perform a hash on the key
# We take the key and run it through the hash, and than we get
# a key value pair back. So we run nails through a mathematical function
# and it returned the number two.

# Two characteristics that are important about HashTables:

# 1. It is one-way, suppose we take "nails" and run it through the hash
# we will get the number two. However, we cannot take the number 2 and retrieve "nails". (One-way only)

# 2. It is deterministic. Which means that for a particular hash function, everytime we put in nails in, we 
# expect to get the number two every time. (It is deterministic.)

# What happens if you end up putting two key-value pairs in the same address? This collision will
# cause an error, so in order for these two pairs to have the same address, what happens is that
# you will create another list at that address, which will contain 2 key-vaue pairs. This practice is called Seperate Chaining.
# Another way of doing seperate chaining is by having a linked list instead of a normal list at each address.

# Another popular way to deal with collision is by finding the next available address to use. You keep on looking until you find 
# a empty spot, this practice is called Linear Probing.

# always aim for a prime number of addresses [0-6], prime numbers always increase the randomness for how the key-value pairs
# are going to be distributed through out the hash table, so it reduces your collisions.

# My Hashtable Class
class HashTable:
    def __init__(self, size = 7):
        # Create a list of 7 items which will contain None
        self.data_map = [None] * size
    
    def __hash__(self, key):
        # Initialize the variable to zero
        my_hash = 0
        # loop through the letters in the key
        for letter in key:
            # for every letter we run this calculation
            # ord() is a func that will retrieve the Ascii number for each letter as we are looping
            # we multiply it by 23 which is a prime number, you can plug in any prime number
            # the real key to this is taking the modulo and dividing it by the length which is 7
            # if you divide any number by 7, the remainder will be any number between 0-6
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i,":", val)
    
my_hash = HashTable()

my_hash.print_table()