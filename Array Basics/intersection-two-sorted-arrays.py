class IntersectionTwoSortedArrays:
    def funtion_BruteForce(self, arr1, arr2): # Space Complexity O(N1)/O(N2) and Time Complexity O(N)
        s1 =set(arr1)
        resArr = []
        for ele in arr2:
            if ele in s1:
                resArr.append(ele)
        
        return resArr

    def function_OptimizedApproach(self, arr1, arr2):
        N1 = len(arr1)
        N2 = len(arr2)
        
        iA1 = 0
        iA2 = 0

        resArr = []

        while iA1 < N1 and iA2 < N2:
            if arr1[iA1] < arr2[iA2]:
                iA1 += 1
            elif arr1[iA1] > arr2[iA2]:
                iA2 += 1
            else:
                resArr.append(arr1[iA1])
                iA1 +=1
                iA2 += 1

        return resArr


if __name__ == "__main__":
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [1, 2, 3, 6, 7]
    print(IntersectionTwoSortedArrays().funtion_BruteForce(arr1, arr2))

    arr1 = [1, 2, 3, 4, 5]
    arr2 = [1, 2, 3, 6, 7]
    print(IntersectionTwoSortedArrays().function_OptimizedApproach(arr1, arr2))