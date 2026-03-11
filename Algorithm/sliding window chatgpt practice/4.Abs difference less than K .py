"""
Sliding Window Problem #4 (Easy)

Problem Statement: Given an integer array nums and an integer k, return true if there are two 
distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k. 
Otherwise, return false.

Example 1:

Input: nums = [1, 2, 3, 1], k = 3

Output: true

Explanation: nums[0] == nums[3] and abs(0 - 3) = 3, which is <= 3.

Example 2:

Input: nums = [1, 2, 3, 1, 2, 3], k = 2

Output: false

Explanation: The duplicates are too far apart. The closest 1s are at index 0 and 3, abs(0 - 3) = 3, which is greater than k.

Constraints:

1 <= nums.length <= 10^5

-10^9 <= nums[i] <= 10^9

0 <= k <= 10^5
"""

class Solution:
    def bruteForce(self, arr, k):
        N = len(arr)

        for i in range(N-k):
            for j in range(i+1, i+k+1):
                if arr[i] == arr[j] and abs(i-j)<=k:
                    return True
        
        return False
    
    def optimalSolution(self, arr, k):
        N = len(arr)

        num_set = set()
        left = 0

        for right in range(N):
            
            while right-left > k:
                num_set.remove(arr[left])
                left += 1
            if arr[right] in num_set:
                return True
            num_set.add(arr[right])

        return False



if __name__ == "__main__":
    nums1 = [1, 2, 3, 1]
    k1 = 3
    sol = Solution()
    print(sol.optimalSolution(nums1, k1))

    nums2 = [1, 2, 3, 1, 2, 3]
    k2 = 2
    print(sol.optimalSolution(nums2, k2))



