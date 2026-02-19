"""
Criteria is that except for 1 number others appears twice in the array.
"""

"""
| Method      | Time Complexity   | Space Complexity |
| ----------- | ----------------- | ---------------- |
| Brute Force | **O(N²)**         | **O(1)**         |
| Hash Array  | **O(N + maxEle)** | **O(maxEle)**    |
| HashMap     | **O(N)**          | **O(N)**         |
| XOR         | **O(N)**          | **O(1)**         |
"""

class FindNumberAppearOnce:
    def findNumber_BruteForce(self, arr):
        N = len(arr)
        for ele in arr:
            countEle = 0
            for j in range(N):
                if arr[j] == ele:
                    countEle += 1 
            if countEle == 1:
                return ele
        
        return -1
    
    def findNumber_BetterApproach(self, arr):
        maxEle = max(arr) # O(N) time taken
        hashArray = [0] * (maxEle+1) # Space complexity is O(maxEle)

        for ele in arr: # O(N) time take in worst case
            hashArray[ele] += 1

        for i in range(len(hashArray)): # O(maxEle) time taken in worst case 
            if hashArray[i] == 1:
                return i
        
        return -1 # Total time taken is O(N+maxEle) in worst case
    
    def findNumber_BetterApproach_withMAP(self, arr):
        N = len(arr) # O(N) time taken

        freqMap = {} # Space Complexity is O(N/2 +1) => O(N)

        for ele in arr: # O(N)
            freqMap[ele] = freqMap.get(ele, 0) + 1
        
        for ele in arr: # O(N)
            if freqMap[ele] == 1:
                return ele
        
        return -1 #Total time complexity O(3N)
    

    def findNumber_Optimzed(self, arr):
        xor = 0
        for ele in arr:
            xor = xor ^ ele
        
        return xor


if __name__ == "__main__":
    arr = [1,1,2,3,3,4,4]
    print(FindNumberAppearOnce().findNumber_BruteForce(arr))
    print(FindNumberAppearOnce().findNumber_BetterApproach(arr))
    print(FindNumberAppearOnce().findNumber_BetterApproach_withMAP(arr))
    print(FindNumberAppearOnce().findNumber_Optimzed(arr))