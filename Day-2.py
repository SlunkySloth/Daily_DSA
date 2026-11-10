"""
LEETCODE 35

Given a sorted array of distinct integers and a target value, 
return the index if the target is found. If not, return the 
index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4
"""
nums = [1,3,5,6]
target = 5
result = 0
right,left = 0, len(nums)-1

while left <= right :
    middle = left+right//2        

    if nums[middle] < target:
        l = m+1
    elif nums[middle] > target:
        r = m - 1
    else:
        print(m)
if nums[m] < target:
    return m + 1
else:
    return m 