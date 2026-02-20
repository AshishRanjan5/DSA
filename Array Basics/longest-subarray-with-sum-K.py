class LongestSubArraySum:
    def funtion_BruteForce(self, arr, K):
        N = len(arr)
        maxCount = 0

        for i in range(N): #O(N)
            for j in range(i, N): # O(N)
                if sum(arr[i:j]) == K: # O(N)
                    maxCount = max(maxCount, j-i)
        
        return maxCount # Total time complexity O(N^3)
    

    def funtion_BetterApproach_then_Brute(self, arr, K):
        N = len(arr)
        maxCount = 0

        for i in range(N): #O(N)
            sumEle = 0
            for j in range(i, N):#O(N)
                sumEle = sumEle + arr[j]
                if sumEle == K:
                    maxCount = max(maxCount, j-i+1)

        return maxCount # Total time complexity O(N^2)
    
    def funtion_BetterApproach_using_HashMAP(self, arr, K):
        prefixSumMap = {}
        currentSum = 0
        maxLen = 0

        for i in range(len(arr)):
            currentSum += arr[i]

            # Case 1: Subarray from 0 to i
            if currentSum == K:
                maxLen = i + 1

            # Case 2: Check if (currentSum - K) exists
            if (currentSum - K) in prefixSumMap:
                length = i - prefixSumMap[currentSum - K]
                maxLen = max(maxLen, length)

            # Store prefix sum if not already present
            if currentSum not in prefixSumMap:
                prefixSumMap[currentSum] = i

        return maxLen
            

    
    def function_OptimizedApproach(self, arr, K):
        N = len(arr)

        left = 0
        currentSum = 0
        maxLen = 0

        for right in range(N):
            currentSum += arr[right]

            # Shrink window while sum is too large
            while currentSum > K and left <= right:
                currentSum -= arr[left]
                left += 1

            # Check if equal
            if currentSum == K:
                maxLen = max(maxLen, right - left + 1)

        return maxLen


if __name__ == "__main__":
    arr = [1,2,3,1,1,1,1,4,2,3]
    print(LongestSubArraySum().funtion_BruteForce(arr, 9))
    print(LongestSubArraySum().funtion_BetterApproach_then_Brute (arr, 9))
    print(LongestSubArraySum().funtion_BetterApproach_using_HashMAP (arr, 9))
    print(LongestSubArraySum().function_OptimizedApproach(arr, 9))