class UnionTwoSortedArray:
    def funtion_BruteForce(self, arr1, arr2):
        for ele in arr2:
            if ele not in arr1:
                arr1.append(ele)
        
        arr1.sort()
        return arr1
    
    def funtion_BruteForce_w_Set(self, arr1, arr2):
        s1 = set(arr1)
        for ele in arr2:
            s1.add(ele)
        
        return list(s1)
    
    def funtion_Optimized_two_Pointer_Approach(self, arr1, arr2):
        N1 = len(arr1)
        N2 = len(arr2)

        iA1 = 0 # index for arr1
        iA2 = 0 # index for arr2

        resArr = []

        while iA1 < N1 and iA2 < N2:
            if arr1[iA1] < arr2[iA2] and arr1[iA1] != resArr[-1]: # crucial to check the arr[i] element with resArr last index.
                resArr.append(arr1[iA1])
                iA1 += 1
            elif arr1[iA1] > arr2[iA2] and arr2[iA2] != resArr[-1]: # crucial to check the arr[i] element with resArr last index.
                resArr.append(arr2[iA2])
                iA2 += 1
            else:
                resArr.append(arr1[iA1])
                iA1 += 1
                iA2 += 1

        while iA1 < N1:
            if resArr[-1] != arr1[iA1]:
                resArr.append(arr1[iA1])
            iA1 += 1
        
        while iA2 < N2:
            if resArr[-1] != arr2[iA2]:
                resArr.append(arr2[iA2])
            iA2 += 1

        return resArr

if __name__ == "__main__":
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [1, 2, 3, 6, 7]
    print(UnionTwoSortedArray().funtion_BruteForce(arr1, arr2))

    arr1 = [1, 2, 3, 4, 5]
    arr2 = [1, 2, 3, 6, 7]
    print(UnionTwoSortedArray().funtion_BruteForce_w_Set(arr1, arr2))

    arr1 = [1, 2, 3, 4, 5]
    arr2 = [1, 2, 3, 6, 7]
    print(UnionTwoSortedArray().funtion_Optimized_two_Pointer_Approach(arr1, arr2))
    


