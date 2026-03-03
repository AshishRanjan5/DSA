"""
Given an array of positive integers nums and an integer target,
return the length of the longest contiguous subarray whose sum is exactly equal to target.

If no such subarray exists, return 0.

Input:
nums = [1, 2, 1, 1, 1]
target = 3

Output:
3

Explanation:
Subarrays with sum = 3:
[1,2]
[2,1]
[1,1,1]

Longest length = 3
"""

nums = [1, 2, 1, 1, 1]
target = 3

max_count = float('-inf')
N = len(nums)

for i in range(N):
    curr_count = 0
    curr_sum = 0
    for j in range(i, N):
        curr_sum += nums[j]
        curr_count += 1
        if curr_sum == target:
            max_count = max(max_count, curr_count)

print(max_count)

left = 0
curr_sum = 0
max_count = float('-inf')
for right in range(N):
    curr_sum += nums[right]
    while curr_sum > target:
        curr_sum -= nums[left]
        left += 1
    if curr_sum == target:
        max_count = max(max_count, right - left + 1)

print(max_count)

