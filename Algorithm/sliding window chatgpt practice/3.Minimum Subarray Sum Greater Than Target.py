"""
Sliding Window Problem #2 (Easy)
Problem Statement: Given an array of positive integers nums and a positive integer target, 
find the minimal length of a contiguous subarray of which the sum is greater than or equal to target. 
If there is no such subarray, return 0 instead.

Example:

Input: target = 7, nums = [2, 3, 1, 2, 4, 3]

Output: 2

Explanation: The subarray [4, 3] has the minimal length under the problem constraint.

Constraints:

1 <= target <= 10^9

1 <= nums.length <= 10^5

1 <= nums[i] <= 10^4
"""

class MinimumSubarraySumGreaterThanTarget:
    def bruteForce(self, nums, target):
        
        N = len(nums)

        minLength = float('inf')
    
        for i in range(N):
            curr_sum = 0
            for j in range(i, N):
                curr_sum += nums[j]
                if curr_sum >= target:
                    minLength = min(minLength, j-i+1)
        
        return minLength
    
    def optimalSolution(self, nums, target):
        N = len(nums)

        minLength = float('inf')
        left = 0
        curr_sum = 0

        for right in range(N):
            curr_sum += nums[right]

            while curr_sum >= target:
                curr_sum -= nums[left]
                minLength = min(minLength, right - left + 1)
                left += 1
            
        return minLength



if __name__ == "__main__":
    nums = [2, 3, 1, 2, 4, 3]
    target = 7
    sol = MinimumSubarraySumGreaterThanTarget()
    print(sol.optimalSolution(nums, target))
