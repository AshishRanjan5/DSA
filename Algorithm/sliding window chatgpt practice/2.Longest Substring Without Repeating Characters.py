"""
Sliding Window Problem #2 (Easy)

Now we'll move to the variable window size pattern, which is the most common one in FAANG interviews.

Problem: Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without repeating characters.

Example 1
Input: s = "abcabcbb"
Output: 3

Explanation:

"abc" → length = 3
Example 2
Input: s = "bbbbb"
Output: 1

Explanation:

"b"
Example 3
Input: s = "pwwkew"
Output: 3

Explanation:

"wke"

Note:

"pwke" is not valid because substring must be contiguous.
Constraints
0 ≤ len(s) ≤ 50,000
s consists of ASCII characters
"""

class LongestRespeatingSubstring:
    def bruteForce(self, s):
        N = len(s)
        longestSubString = ""
        maxCount = 0
        for i in range(N):
            currSubstring = ""
            currCount = 0
            for j in range(i, N):
                if s[j] not in currSubstring:
                    currSubstring += s[j]
                    currCount += 1
                else:
                    break
            
            if maxCount < currCount:
                maxCount = max(currCount, maxCount)
                longestSubString = currSubstring
        
        return maxCount

    
    def optimalSolution(self, s):
        char_set = set()

        left = 0
        N = len(s)
        maxCount = 0

        for right in range(N):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            
            
            char_set.add(s[right])
            maxCount = max(maxCount, right - left + 1)
        
        return maxCount


if __name__ == "__main__":
    s = "pwwkew"
    sol = LongestRespeatingSubstring()
    print(sol.optimalSolution(s))

