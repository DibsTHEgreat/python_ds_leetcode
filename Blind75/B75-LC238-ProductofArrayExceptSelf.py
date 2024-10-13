# Leetcode 238: Product of Array Except Self
# Problem List: Blind 75
# Topics: Array & Prefix Sum

# Time Complexity: O(N)
# Space Complexity: O(1)

from typing import List

class Solution:
    def productExpectSelf(self, nums: List[int]) -> List[int]:
        # Create the result array initialized with 1s, same length as nums.
        # This does not count as extra memory because it's the required output.
        result = [1] * len(nums)
        
        # Variable to store the prefix product
        prefix = 1
        
        # First pass: Calculate the prefix product for each element
        for i in range(len(nums)):
            # Set result[i] to the prefix product before the current element
            result[i] = prefix
            
            # Update prefix by multiplying it with the current element
            prefix *= nums[i]
        
        # Variable to store the postfix product
        postfix = 1
        
        # Second pass: Calculate the postfix product for each element
        # and multiply it with the existing value in the result
        # Syntax explanation: range(start, stop, step)
            # Start: Starting at the last index value
            # Stop: Stopping before -1 a.k.a stop at 0
            # Step: move -1 times, as in move back 1 step
        for i in range(len(nums) - 1, -1, -1):
            # Multiply the current result[i] by the postfix product
            result[i] *= postfix
            
            # Update postfix by multiplying it with the current element
            postfix *= nums[i]
        
        # Return the result array
        return result