"""
Problem Statement: Given a binary array nums (containing only 0s and 1s) and an integer k, 
return the maximum number of consecutive 1s in the array if you can flip at most k 0s.

Example 1:

Input: nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], k = 2

Output: 6

Explanation: [1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1]
We flipped the 0s at index 5 and 10 from the original array. The longest subarray of 1s is length 6.

Constraints:

1 <= nums.length <= 10^5

nums[i] is either 0 or 1.

0 <= k <= nums.length
"""

class MinimumSubarraySumGreaterThanTarget:
    def bruteForce(self, nums, k):
        N = len(nums)
        max_count = float('-inf')
        
        for i in range(N):
            char_freq = {}
            curr_count = 0
            for j in range(i, N):
                char_freq[nums[j]] = char_freq.get(nums[j], 0) + 1
                curr_count += 1
            
            if char_freq.get(0, 0) <= k:
                max_count = max(max_count, curr_count)
        
        return max_count

    def optimalSolution(self, nums, k):
        N = len(nums)
        max_count = float('-inf')

        left = 0
        char_freq = {}

        for right in range(N):
            char_freq[nums[right]] = char_freq.get(nums[right], 0) + 1

            while char_freq.get(0, 0) > k:
                char_freq[nums[left]] -= 1
                left += 1
            
            max_count = max(max_count, right - left + 1)
        
        return max_count
    
    def optimalSolutionFixedSpace(self, nums, k):
        N = len(nums)
        max_count = float('-inf')

        left = 0
        zero_count = 0

        for right in range(N):
            if nums[right] == 0:
                zero_count += 1

            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
                
            
            max_count = max(max_count, right - left + 1)
        
        return max_count


if __name__ == "__main__":
    nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
    k = 2
    sol = MinimumSubarraySumGreaterThanTarget()
    print(sol.optimalSolutionFixedSpace(nums, k))