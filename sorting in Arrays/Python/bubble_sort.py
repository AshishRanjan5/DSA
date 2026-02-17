class BubbleSort:
    def sortArray(self, arr):
        for i in range(len(arr)):
            for j in range(len(arr)):
                if arr[j] > arr[i]: # arr[j] < arr[i] for descending order
                    arr[i], arr[j] = arr[j], arr[i]
        

        


if __name__ == "__main__":
    arr = [2, 4, 1, 3, 5]
    BubbleSort().sortArray(arr)
    print(arr)
