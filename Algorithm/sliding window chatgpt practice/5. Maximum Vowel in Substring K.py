"""
Sliding Window Problem #5 (Easy/Medium)
Problem Statement: Given a string s and an integer k, return the maximum number of vowel letters 
in any substring of s with length k. Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

Example 1:

Input: s = "abciiidef", k = 3

Output: 3

Explanation: The substring "iii" contains 3 vowel letters.

Example 2:

Input: s = "leetcode", k = 3

Output: 2

Explanation: "lee", "eet" and "ode" contain 2 vowels.

Constraints:

1 <= s.length <= 10^5

s consists of lowercase English letters.

1 <= k <= s.length
"""

class MaximumVowelSubstringK:
    def bruteForce(self, s, k):
        N = len(s)
        vowels = set({'a', 'e', 'i', 'o', 'u'})

        maxVowel = float('-inf')

        for i in range(N-k+1):
            countVowel = 0
            for j in range(i, i+k):
                if s[j] in vowels:
                    countVowel += 1
            maxVowel = max(maxVowel, countVowel)
        
        return maxVowel


    def optimalSolution(self, s, k):
        N = len(s)
        vowels = set({'a', 'e', 'i', 'o', 'u'})

        curr_count = 0

        for i in range(k):
            if s[i] in vowels:
                curr_count += 1
        
        max_count = curr_count

        for right in range(k, N):
            if s[right] in vowels:
                curr_count += 1
            
            if s[right-k] in vowels:
                curr_count -= 1
            
            max_count = max(max_count, curr_count)
        
        return max_count

if __name__ == "__main__":
    s = "abciiidef"
    k = 3
    sol = MaximumVowelSubstringK()
    print(sol.optimalSolution(s, k))



