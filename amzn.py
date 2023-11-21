#AMAZON Leetcode#
# https://github.com/hxu296/leetcode-company-wise-problems-2022#amazon
#################
#https://www.geeksforgeeks.org/bisect-algorithm-functions-in-python/
#https://cc189.github.io/leetcode/users/hiepit
import bisect
class Solution:
    # Two Sum - LC1 (Easy)
    def twoSum(self, nums, target):
        complement = {} # initialize an empty dictionary
        for i, num in enumerate(nums): # loop through each element of the array
            if num in complement: # check if the element is in the dictionary
                return [complement[num], i] # return the indices as the answer
            else: # otherwise
                complement[target - num] = i # store the complement and the index in the dictionary
        return [] # return an empty list if no match is found


    # LRU Cache
    # Number of Islands - LC200 (Medium)
    def numIslands(self, grid) -> int:
        count = 0
        # loop through each cell of the grid
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # check if the cell is a land cell
                if grid[i][j] == '1':
                    # increment the count of islands
                    count += 1
                    # mark the adjacent land cells as '0'
                    self.dfs(grid, i, j, len(grid), len(grid[0]))
        return count
   
    def dfs(self, grid, i, j, m, n):
        # check if the row and column indices are valid and the cell is a land cell
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == '0':
            return
        # mark the cell as '0'
        grid[i][j] = '0'
        # recursively call dfs on the four neighboring cells
        self.dfs(grid, i - 1, j, m, n)
        self.dfs(grid, i + 1, j, m, n)
        self.dfs(grid, i, j - 1, m, n)
        self.dfs(grid, i, j + 1, m, n)
# Merge Intervals - LC56 (Medium)
#https://johngrant.medium.com/python-list-sorting-keys-lambdas-1903b2a4c949
    def merge_intervals(self, intervals):
        # Sort the intervals by start time
        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            # If the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, append it
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # Otherwise, there is overlap, so we merge the current and previous
                # intervals by updating the end time of the previous interval
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged
    # Search Suggestions System - LC1268
    '''
    You are given an array of strings products and a string searchWord.

    Design a system that suggests at most three product names from products after each character of searchWord is typed. Suggested products should have common prefix with searchWord. If there are more than three products with a common prefix return the three lexicographically minimums products.

    Return a list of lists of the suggested products after each character of searchWord is typed.
    '''
    
    def suggested_products(self, products, searchWord):
        products.sort()
        result, prefix = [], ''
        for char in searchWord:
            prefix += char
            i = bisect.bisect_left(products, prefix)
            result.append([product for product in products[i:i+3] if product.startswith(prefix)])
        return result


# Best Time to Buy and Sell Stock -LC121

# Group Anagrams
# Analyze User Website Visit Pattern
# Longest Substring Without Repeating Characters
# K Closest Points to Origin
# Meeting Rooms II
# Merge k Sorted Lists
# Trapping Rain Water
# 3Sum
# Valid Parentheses
# Word Ladder
# Median of Two Sorted Arrays
# Add Two Numbers
# Word Search
# Maximum Subarray

if __name__ == "__main__":

#two sum - LC1
    p1 = (2,7,11,15)
    t1 = 9
    s1 = Solution()
    #print(s1.twoSum(p1, t1))

#number of island - LC200
    grid200 = [
            ["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]]
    s200 = Solution()
    #print(s200.numIslands(grid200))

#merge intervals - LC56
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
s56 = Solution()
#print(s56.merge_intervals(intervals))

# suggested product - LC 1268
products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
searchWord = "mouse"

s1268 = Solution()
print(s1268.suggested_products(products, searchWord))
