"""
Maximum Sum Subarray of Size K

Problem:

Given an array of integers nums and an integer k,
return the maximum sum of any contiguous subarray of size k.

Example:
Input:
nums = [2, 1, 5, 1, 3, 2]
k = 3

Output:
9

Explanation:
[5,1,3] has maximum sum = 9
Constraints:

1 ≤ k ≤ n ≤ 10^5

Elements can be negative or positive.
"""

nums = [2, 1, 5, 1, 3, 2]
k = 3
max_sum = float('-inf')

for i in range(0, len(nums)-k+1):
    curr_sum = 0
    for j in range(i, i + k):
        curr_sum += nums[j]
    
    if curr_sum >= max_sum:
        max_sum = curr_sum

print(max_sum)

left = 0
max_sum = sum(nums[:k])
curr_sum = max_sum
for right in range(k, len(nums)):
    curr_sum = curr_sum + nums[right] - nums[left]
    left += 1
    if curr_sum > max_sum:
        max_sum = curr_sum

print(max_sum)
