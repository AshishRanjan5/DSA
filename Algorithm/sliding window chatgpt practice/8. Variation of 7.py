"""
Sliding Window Problem #8 (Medium)
Problem Statement: Given a binary array nums (containing only 0s and 1s) and an integer k, return the length of the 
shortest contiguous subarray that contains exactly k 0s. If no such subarray exists, return 0.

Example 1:

Input: nums = [1, 1, 0, 1, 1, 0, 1, 0, 1], k = 2

Output: 4

Explanation: The subarray [0, 1, 1, 0] has exactly two 0s and a length of 4. There is also [0, 1, 0] which has a length of 3. 
The shortest is [0, 1, 0], wait, let me look at the array again. The zeros are at indices 2, 5, and 7.

Zeros at index 2 and 5: subarray [0, 1, 1, 0] (length 4)

Zeros at index 5 and 7: subarray [0, 1, 0] (length 3)
The shortest valid subarray is length 3.

Example 2:

Input: nums = [1, 0, 0, 1, 0], k = 3

Output: 4

Explanation: The subarray [0, 0, 1, 0] has exactly three 0s and is the shortest.

Example 3:

Input: nums = [1, 1, 1], k = 1

Output: 0

Explanation: There are no 0s in the array, so we return 0.

Constraints:

1 <= nums.length <= 10^5

nums[i] is either 0 or 1.

1 <= k <= nums.length
"""

class ShortestSubarrayExactlyk0s:
    def bruteForce(self, arr, k):
        min_len = float('inf')
        n = len(arr)

        for i in range(n):

            zero_count = 0

            for j in range(i, n):

                if arr[j] == 0:
                    zero_count += 1

                if zero_count == k:
                    min_len = min(min_len, j - i + 1)

                if zero_count > k:
                    break

        return 0 if min_len == float('inf') else min_len
    
    def optimalSolution(self, arr, k):
        min_count = float('inf')
        left = 0
        zero_count = 0
        
        for right in range(len(arr)):
            # 1. Reflect reality
            if arr[right] == 0:
                zero_count += 1

            # 2. Fix reality & Optimize for shortest length
            # We shrink if we break the rule (too many 0s) 
            # OR if we have dead weight (the left element is a 1)
            while left <= right and (zero_count > k or arr[left] == 1):
                if arr[left] == 0:
                    zero_count -= 1
                left += 1
            
            # 3. Record (only if the condition is perfectly met)
            if zero_count == k:
                min_count = min(min_count, right - left + 1)
        
        return 0 if min_count == float('inf') else min_count

if __name__ == "__main__":
    arr = [1, 1, 0, 1, 1, 0, 1, 0, 1]
    k = 2
    sol = ShortestSubarrayExactlyk0s()
    print(sol.bruteForce(arr, k))
