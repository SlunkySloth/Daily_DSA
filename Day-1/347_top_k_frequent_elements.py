#This is the note taker and problem solving on all the neetcode 150 problems.

"""
##347. Top K Frequent Elements
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:
Input: nums = [1], k = 1
Output: [1]
Example 3:
Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2
Output: [1,2]
"""
from collections import Counter
nums = [1,2,1,2,1,2,3,1,3,2]
k = 2
result = []
count = Counter(nums)
for number,count in count.most_common(k):
    result.append(number)
print(result)

"""
we import the counter module and 
--counter tells the no of times that the number are repeated and it is stored in a dictionary 
{number:times it is reapeated}
{1:2,2:3}
we create a for loop to appenf the most numbers in the array
"""



