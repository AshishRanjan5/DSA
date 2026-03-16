"""
Sliding Window Problem #9 (Hard)
Problem Statement: You are given an array of integers nums. There is a sliding window of size k which 
is moving from the very left of the array to the very right. You can only see the k numbers in the window. 
Each time the sliding window moves right by one position. Return the maximum sliding window 
(an array containing the maximum value of each window step).

Example 1:

Input: nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3

Output: [3, 3, 5, 5, 6, 7]

Explanation:

Plaintext
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Constraints:

1 <= nums.length <= 10^5

-10^4 <= nums[i] <= 10^4

1 <= k <= nums.length
"""

class Solution:
    def bruteForce(self, nums, k):
        
        N = len(nums)
        max_array = []

        for i in range(N-k+1):
            curr_max = max(nums[i:i+k])
            
            max_array.append(curr_max)
        
        return max_array
    
    def optimalApproach(self, nums, k):
        from collections import deque
        N = len(nums)

        max_array = []
        dq = deque()

        for i in range(N):
            if dq and dq[0] <= i-k:
                dq.popleft()
            
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()
            
            dq.append(i)

            if i >= k-1:
                max_array.append(nums[dq[0]])
        
        return max_array


if __name__ == "__main__":
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    sol = Solution()
    print(sol.optimalApproach(nums, k))