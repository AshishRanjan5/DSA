class SelectionSort:
  def sortArray(self, arr):
    for i in range(len(arr)):
      minValue = arr[i]
      minIndex = i
      for j in range(i+1, len(arr)):
        if arr[j] < minValue:
          minValue = min(arr[j], minValue) 
          minIndex = j
      arr[i], arr[minIndex] = arr[minIndex], arr[i]
    print(arr)

if __name__ == "__main__":
  selectSort = SelectionSort()
  selectSort.sortArray([2, 4, 1, 3, 5])