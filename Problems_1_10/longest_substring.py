def longest_substring(s):
    char_index_map = {}
    start = 0
    max_length = 0
    longest_sub = ""

    for end in range(len(s)):
        if s[end] in char_index_map and char_index_map[s[end]] >= start:
            start = char_index_map[s[end]] + 1
        
        char_index_map[s[end]] = end
        current_length = end - start + 1
        
        if current_length > max_length:
            max_length = current_length
            longest_sub = s[start:end+1]
    
    return max_length

# Example usage:
s = "pwwkew"
print(longest_substring(s))  # Output: "wke"
