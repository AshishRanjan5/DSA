class OperationsOnArray:
    def maxElement(self, arr):
        maxEle = arr[0]
        for ele in arr[1:]:
            if ele >= maxEle:
                maxEle = ele

        return maxEle

    def SecondLargestElement(self, arr):
        maxEle = arr[0]
        secondMaxEle = arr[0]

        for ele in arr[1:]:
            if ele>maxEle:
                secondMaxEle = maxEle
                maxEle = ele
            elif ele>secondMaxEle:
                secondMaxEle = ele

        return secondMaxEle
                



if __name__ == "__main__":
    arr = [2, 4, 1, 3, 5]
    print(OperationsOnArray().maxElement(arr))
    print(OperationsOnArray().SecondLargestElement(arr))
