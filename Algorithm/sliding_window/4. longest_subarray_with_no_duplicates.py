"""
Longest Substring Without Repeating Characters

Input:

s = "abcabcbb"

Output:

3
"""

s = "abcabcbb"

# Brute Force

N = len(s)
max_length = float('-inf')
for i in range(N):
    char_set = set()
    subS = ""
    for j in range(i, N):
        if s[j] not in char_set:
            subS += s[j]
            char_set.add(s[j])
        else:
            break
    
    max_length = max(max_length, len(subS))

print(max_length)

char_set = set()
left = 0
max_length = 0

for right in range(N):

    while s[right] in char_set:
        char_set.remove(s[left])
        left += 1
    
    char_set.add(s[right])
    max_length = max(max_length, right-left+1)

print(max_length)





