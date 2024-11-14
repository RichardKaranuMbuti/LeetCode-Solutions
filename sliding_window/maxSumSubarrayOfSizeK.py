"""
Problem
Given an array of positive integers and an integer 
𝐾
K, find the maximum sum of any contiguous subarray of size 
𝐾
K.

Explanation
Imagine you have a fixed-size "window" of 
𝐾
K elements. You want to slide this window across the array, moving one element at a time, and find the highest sum within any window of size 
𝐾
K.

Example
Input: arr = [2, 1, 5, 1, 3, 2], K = 3
Output: 9
How It Works
First Window Calculation: Calculate the sum of the first 
𝐾
K elements (i.e., [2, 1, 5]). This sum is 2 + 1 + 5 = 8.
Sliding the Window: Slide the window one element to the right. Subtract the element that goes out of the window (left side) and add the element that comes into the window (right side).
For the next window [1, 5, 1], the sum is 8 - 2 + 1 = 7.
For the next window [5, 1, 3], the sum is 7 - 1 + 3 = 9 (the maximum sum so far).
Continue sliding until you've covered all subarrays of size 
𝐾
K.
"""

def maxSumSubarrayOfSizeK(arr, k):
    window_sum = 0
    max_sum = 0 
    
    # Step 1: calculate the sum of the first window
    for i in range(k):
        window_sum += arr[i]
    max_sum = window_sum

    # Step 2: Slide the window through the array
    # we add to window sum one element to right and sub one element from left to maintain size of the window
    # index of  item to the left is given by current index - size of the window
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i-k] + arr[i]
        max_sum = max(max_sum,window_sum)
    return max_sum

# Example
arr = [2, 1, 5, 1, 3, 2]
K = 3
print(maxSumSubarrayOfSizeK(arr, K))  # Output: 9
"""
Time complexity is O(n):because each element is added and removed from the sum once.
Space complexity is O(1): only storing the current window sum
"""

