class BubbleSort:
    def sortArray(self, arr):
        for i in range(len(arr)):
            for j in range(len(arr)-i-1):
                if arr[j+1] < arr[j]: # arr[j+1] > arr[i] for descending order
                    arr[j+1], arr[j] = arr[j], arr[j+1]
        

        


if __name__ == "__main__":
    arr = [2, 4, 1, 3, 5]
    BubbleSort().sortArray(arr)
    print(arr)
