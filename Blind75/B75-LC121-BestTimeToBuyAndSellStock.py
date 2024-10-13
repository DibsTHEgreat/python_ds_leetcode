# Leetcode 121: Best Time to Buy and Sell Stock
# Problem List: Blind 75
# Topics: Array & Dynamic Programming

# Using two-pointer style

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # left is meant for buying (index of the day you will buy the stock)
        left = 0
        
        # right is for selling (index of the day you will try to sell the stock)
        right = 1

        maxP  = 0
        
        # Loop until the right pointer reaches the end of the prices array
        while right < len(prices):
            
            # Check if it's profitable to sell on the right day (prices[right])
            if prices[left] < prices[right]:
                # Calculate the profit if we bought at left and sold at right
                profit = prices[right] - prices[left]
                # Update the maximum profit if the current profit is greater
                maxP = max(maxP, profit)
            else:
                # If not profitable, move the left pointer to the right pointer's position
                # This means we will consider buying at this new point on the next iteration
                left = right
            
            # Move the right pointer to the next day to check a new selling possibility
            right += 1
        
        return maxP
        