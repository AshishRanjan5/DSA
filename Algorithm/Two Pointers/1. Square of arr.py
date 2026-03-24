"""
Given a sorted array nums (can have negative numbers), return an array of the squares of each number in sorted order

Example
nums = [-4, -1, 0, 3, 10]
Output = [0,1,9,16,100]
"""

class Solution:
    def squareArr(self, nums):
        N = len(nums)
        left = 0
        right = N - 1

        res = [0] * N
        pos = right

        while left <= right:
            if abs(nums[left]) < abs(nums[right]): # we could do this just because we have most negative and most positive at extreme left and right corners of the arr.
                res[pos] = nums[right] ** 2
                right -= 1
            else:
                res[pos] = nums[left] ** 2
                left += 1
            
            pos -= 1
        
        return res

if __name__ == "__main__":
    nums = [-4, -1, 0, 3, 10]
    print(Solution().squareArr(nums))