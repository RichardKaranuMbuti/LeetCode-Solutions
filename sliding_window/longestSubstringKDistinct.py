"""
Problem
Given a string s and an integer 
K, find the length of the longest substring that contains at most 

K distinct characters.

Explanation
In this case, we use a variable-size window. We expand the window by including new
 characters until the window has more than 

K distinct characters. Once it exceeds 

K, we shrink the window from the left until we’re back to 

K distinct characters.

Example
Input: s = "araaci", K = 2
Output: 4 (The substring "araa" has length 4 and only 2 distinct characters).
How It Works
Expand the Window: Start with an empty window, add characters from the string while
 tracking the count of each character (using a hashmap).
Exceeding 

K Distinct Characters: When you have more than 

K distinct characters in the window, shrink it from the left by moving the starting
 point until you’re back to 

K or fewer distinct characters.
Track the Length: Throughout, keep track of the maximum length of any valid window
 (with at most 

K distinct characters).
"""

def longestSubstringKDistinct(s, k):
    start = 0
    max_length = 0
    char_count = {}

    for end in range(len(s)):
        right_char = s[end]
        char_count[right_char]=char_count.get(right_char, 0)+1

        # Shrink the window untill we have <= k distinct characters
        while len(char_count) > k:
            left_char = s[start]
            char_count[left_char] -= 1
            if char_count[left_char] == 0:
                del char_count[left_char]
            start +=1

        #Update the size of min length of valid substring
        max_length = max(max_length, end-start+1)
    return max_length


