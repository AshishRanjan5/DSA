"""
First Negative Number in Every Window of Size K

Example

nums = [12, -1, -7, 8, -15, 30, 16, 28]
k = 3

Output:
[-1, -1, -7, -15, -15, 0]
"""
nums = [12, -1, -7, 8, -15, 30, 16, 28]
k = 3
res = []
N = len(nums)

for i in range(N-k+1):
    for j in range(i, i+k):
        if nums[j] < 0:
            res.append(nums[j])
            break

print(res)


from collections import deque

dq = deque()
res = []

for right in range(N):
    
    # Step 1: Add new negative
    if nums[right] < 0:
        dq.append(right)
    
    # Step 2: Remove indices outside window
    if dq and dq[0] < right - k + 1:
        dq.popleft()
    
    # Step 3: Record result if window is full
    if right >= k - 1:
        if dq:
            res.append(nums[dq[0]])
        else:
            res.append(0)

print(res)
