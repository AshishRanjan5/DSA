"""
Sliding Window Problem #1 (Easy)
Problem: Maximum Sum Subarray of Size K

You are given an array of integers and a number k.
Find the maximum sum of any contiguous subarray of size k.

Example

Input

arr = [2, 1, 5, 1, 3, 2]
k = 3

Output

9

Explanation

Subarrays of size 3:

[2,1,5] = 8
[1,5,1] = 7
[5,1,3] = 9  ← maximum
[1,3,2] = 6

So the answer is 9.

Constraints

1 ≤ k ≤ len(arr)

-10^4 ≤ arr[i] ≤ 10^4

len(arr) can be large (up to ~10⁵)
"""

class MaxSubarraySumSizeK:
    def bruteForce(self, arr, k):
        max_sum = float('-inf')
        N = len(arr)
        
        for i in range(N-k+1):
            curr_sum = 0
            for j in range(i, i+k):
                curr_sum += arr[j]
            
            max_sum = max(curr_sum, max_sum)

        return max_sum
    
    def optimalSolution(self, arr, k):
        N = len(arr)

        left = 0
        curr_sum = sum(arr[:k])
        max_sum = curr_sum

        for right in range(k, N):
            curr_sum += arr[right] - arr[left]
            max_sum = max(max_sum, curr_sum)
            left += 1 
        
        return max_sum

if __name__ == "__main__":
    arr = [2, 1, 5, 1, 3, 2]
    k = 3
    sol = MaxSubarraySumSizeK()
    print(sol.optimalSolution(arr, k))


