
"""
Given an array of integers nums and an integer target, return indices of the two numbers 
such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same 
element twice.

You can return the answer in any order.
Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
"""

# Approach 1: Hash map for memoization 
# Time complexity is 0(n)
def sumoftwo(nums, target):
    found_nums = {}
    for i, num in enumerate(nums):
        complement = target-num
        if complement in found_nums:
            return [found_nums[complement], i]
        found_nums[num]= i
    return []

# Example usage
nums1 = [2, 7, 11, 15,]
target1 = 9
print(sumoftwo(nums1, target1))

nums = [2, 7, 11, 15,]

# Approach 2: two pointer approach with time complexity O(n log n)
def twosum(nums, target):
    indexed_nums = [(num, i) for i,num in enumerate(nums)]
    indexed_nums.sort()
    left= 0
    right = len(nums)-1

    while left<right:
        current_sum = indexed_nums[left][0]+ indexed_nums[right][0]
        if current_sum==target:
            return[indexed_nums[left][1], indexed_nums[right][1]]
        elif current_sum < target:
            left +=1
        else:
            right -=1

target = 9      
twosum(nums, target)



