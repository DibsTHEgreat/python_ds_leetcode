# Leetcode 217: Contains Duplicates
# Problem List: Blind 75
# Topics: Array, Hash Table, & Sorting

# Time Complexity: O(N)
# Space Complexity: O(N)

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Initialize an empty set to keep track of unique elements
        hashSet = set()
        # Iterate through each element in the array
        for n in nums:
            # Check if the element is already in the set
            if n in hashSet:
                # Return True if duplicates found
                return True
            # If it's not, add the element to the set
            hashSet.add(n)
        # Return False if no duplicates found
        return False
