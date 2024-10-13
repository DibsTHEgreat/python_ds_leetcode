# Leetcode 152: Maximum Product Subarray
# Problem List: Blind 75
# Topics: Array, & Dynamic Programming

# Time Complexity: O(N)
# Space Complexity: O(1)

from typing import List

def maxProduct(self, nums: List[int]) -> int:
    # we don't init to 0, because there could be an edge case where the only
    # element in the array is -1, so 0 is not a good default value
    result = max(nums)
    
    # 1 is like a netural value
    curMin = 1
    curMax = 1
    
    for n in nums:
        # If the current number is 0, reset curMax and curMin to 1 and skip to the next number.
        # This is because multiplying by 0 would reset the product to 0, and it won't contribute to a maximum product.
        if n == 0:
            curMax = 1
            curMin = 1
            continue
        
        # Store the current maximum product temporarily because curMax will be updated.
        temp = curMax * n
        
        # Update curMax by considering:
        # 1. n * curMax: Extending the current maximum product
        # 2. n * curMin: Extending the current minimum product (which might turn positive if n is negative)
        # 3. n: Starting a new product subarray with the current number
        curMax = max(n * curMax, n * curMin, n)
        
        # Update curMin similarly to track the minimum product.
        curMin = min(temp, n * curMin, n)
        
        # Update the result to hold the maximum product found so far.
        result = max(result, curMax)
    
    return result
    
    