# Leetcode 153: Find Minimum in Rotated Sorted Array
# Problem List: Blind 75
# Topics: Array & Binary Search

# Time Complexity: O(log n)
# Space Complexity:

# Need to use a modified version of the Binary Search Algorithm

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Start by assuming the smallest element is the first element
        result = nums[0]
        
        # Set the left and right pointers to the start and end of the array
        left = 0
        right = len(nums) - 1
        
        # Continue searching while there are elements between left and right pointers
        while left <= right:
            # If the array is already sorted between the left and right pointers, 
            # the smallest element is the leftmost element in this subarray.
            if nums[left] < nums[right]:
                # Update the result to be the smaller of the current result or the leftmost element
                result = min(result, nums[left])
                break
            
            # If the edge case above does not happen than we...
            # Calculate the middle index of the current subarray
            midPointer = (left + right) // 2
            
            # Update the result with the minimum of the current result and the middle element
            result = min(result, nums[midPointer])
            
            # If the middle element is greater than or equal to the left element, 
            # this means the left side is sorted, and the minimum must be in the right half
            if nums[midPointer] >= nums[left]:
                left = midPointer + 1
            else:
                # Otherwise, the minimum must be in the left half, so adjust the right pointer
                right = midPointer - 1
            
            return result