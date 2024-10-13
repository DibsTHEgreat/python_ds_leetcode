# Leetcode 1: Two Sum
# Problem List: Blind 75
# Topics: Array & HashTable

from typing import List

class Solution:
    def twoSum(self, nums:  List[int], target: int) -> List[int]:
        # This dictionary (hashmap) will store numbers we've seen so far as keys,
        # and their corresponding indices as values.
        elementsCovered = {}
        
        # Loop through the list 'nums' using enumerate to get both the index (i) and the number (n).
        for i, n in enumerate(nums):      
            # Calculate the difference needed to reach the target when added to the current number.
            diff = target - n
            
            # Check if this difference is already in the dictionary. 
            # If it is, it means we found two numbers that add up to the target.
            if diff in elementsCovered:
                # Return the indices of the two numbers: 
                # one we've seen before (`elementsCovered[diff]`) and the current index (`i`).
                return [elementsCovered[diff], i]
            
            # If not, add the current number and its index to the dictionary for future reference.
            elementsCovered[n] = i
            
        # In case no two numbers add up to the target, the function will return None (implicitly).
        return None