class OperationsOnArray:
    def maxElement(self, arr):
        maxEle = arr[0]
        for ele in arr[1:]:
            if ele >= maxEle:
                maxEle = ele

        return maxEle
    
    def minElement(self, arr):
        minEle = float('inf')
        for ele in arr:
            if ele < minEle:
                minEle = ele
        
        return minEle

    def secondLargestElement(self, arr):
        maxEle = arr[0]
        secondMaxEle = arr[0]

        for ele in arr[1:]:
            if ele>maxEle:
                secondMaxEle = maxEle
                maxEle = ele
            elif ele>secondMaxEle:
                secondMaxEle = ele

        return secondMaxEle
    
    def secondSmallestElement(self, arr):
        minEle = float('inf')
        secondMinEle = float('inf')

        for ele in arr:
            if ele<minEle:
                secondMinEle = minEle
                minEle = ele
            elif ele<secondMinEle:
                secondMinEle = ele
        
        return secondMinEle
    
    def thirdLargestElement(self, arr):
        maxEle = arr[0]
        secondMaxEle = arr[0]
        thirdMaxEle = arr[0]

        for ele in arr[1:]:
            if ele>maxEle:
                thirdMaxEle = secondMaxEle
                secondMaxEle = maxEle
                maxEle = ele
            elif ele>secondMaxEle:
                thirdMaxEle = secondMaxEle
                secondMaxEle = ele
            elif ele>thirdMaxEle:
                thirdMaxEle = ele
        
        return thirdMaxEle
    
    def isSorted(self, arr):
        for i in range(len(arr)-1):
            if arr[i+1] < arr[i]:
                return False
        
        return True
    
    def removeDuplicates(self, arr):
        res = [arr[0]]

        for i in range(1, len(arr)):
            if arr[i] != arr[i-1]:
                res.append(arr[i])
        
        return res
                



if __name__ == "__main__":
    arr = [2, 4, 1, 3, 5]
    print(OperationsOnArray().maxElement(arr))
    print(OperationsOnArray().secondLargestElement(arr))
    print(OperationsOnArray().thirdLargestElement(arr))
    print(OperationsOnArray().minElement(arr))
    print(OperationsOnArray().secondSmallestElement(arr))
    arr2 = [1,2,3,4,5]
    print(OperationsOnArray().isSorted(arr))
    print(OperationsOnArray().isSorted(arr2))

    arr3 = [1, 1, 1, 2, 3, 3, 4, 5, 5]
    print(OperationsOnArray().removeDuplicates(arr3))
