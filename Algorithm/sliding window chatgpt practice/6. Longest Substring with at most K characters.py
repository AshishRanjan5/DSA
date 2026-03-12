"""
Sliding Window Problem #6 (Medium)
Problem Statement: Given a string s and an integer k, return the length of the longest substring of s that contains at most k distinct characters.

Example 1:

Input: s = "eceba", k = 2

Output: 3

Explanation: The substring is "ece" with length 3 (it contains 2 distinct characters: 'e' and 'c').

Example 2:

Input: s = "aa", k = 1

Output: 2

Explanation: The substring is "aa" with length 2.

Constraints:

1 <= s.length <= 5 * 10^4

0 <= k <= 50
"""

class LongestRespeatingSubstring:
    def bruteForce(self, s, k):
        N = len(s)
        
        max_count = float('-inf')

        for i in range(N):
            curr_count = 0
            char_set = set()
            for j in range(i, N):
                char_set.add(s[j])
                if len(char_set) <= k:
                    curr_count += 1
                else:
                    break
            max_count = max(max_count,curr_count)
        
        return max_count

    def optimalSolution(self, s, k):
        N = len(s)
        max_count = float('-inf')
        
        charFreq = {}

        left = 0

        for right in range(N):
        
            charFreq[s[right]] = charFreq.get(s[right], 0) + 1
            
            while len(charFreq) > k:
                charFreq[s[left]] -= 1
                if charFreq[s[left]] == 0:
                    del charFreq[s[left]]
                left += 1
            
            max_count = max(max_count, right - left + 1)
        
        return max_count

if __name__ == "__main__":
    s1 = "eceba"
    k1 = 2

    s2 = "aa"
    k2 = 1
    sol = LongestRespeatingSubstring()
    print(sol.optimalSolution(s1, k1))
    print(sol.optimalSolution(s2, k2))

