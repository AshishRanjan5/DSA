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
        pass


    def optimalSolution(self, s, k):
        N = len(s)
        pass

if __name__ == "__main__":
    s = "eceba"
    k = 2
    sol = LongestRespeatingSubstring()
    print(sol.optimalSolution(s, k))

