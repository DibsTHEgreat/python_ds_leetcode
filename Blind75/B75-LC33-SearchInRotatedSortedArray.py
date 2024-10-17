# Leetcode 33: Search in Rotated Sorted Array
# Problem List: Blind 75
# Topics: Array, and Binary Search

# Time Complexity: O(log n)
# Space Complexity:

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Initialize pointers to define the search space
        left = 0
        right = len(nums) - 1
        
        # Continue searching while there are elements between left and right
        while left <= right:
            # Calculate the middle index of the current search range
            middle = (left + right) // 2
            
            # If the target is at the middle, return its index
            if target == nums[middle]:
                return middle
            
            # Determine if the left portion is sorted
            if nums[left] <= nums[middle]:
                # Check if the target is not within the sorted left portion
                if target > nums[middle] or target < nums[left]:
                    # Move to the right side of the array
                    left = middle + 1
                else:
                    # Search within the left side of the array
                    right = middle - 1
            # Otherwise, the right portion must be sorted
            else:
                # Check if the target is not within the sorted right portion
                if target < nums[middle] or target > nums[right]:
                    # Move to the left side of the array
                    right = middle - 1
                else:
                    # Search within the right side of the array
                    left = middle + 1
        # If the target is not found, return -1
        return -1