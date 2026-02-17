class KthLargestElement:
  def thirdLargestElement(self, arr):
    
    if len(arr)< 3:
      return -1
    first = float('-inf')
    second = float('-inf')
    third = float('-inf')

    for ele in arr:
      if ele > first:
        third = second
        second = first
        first = ele
      elif ele > second:
        third = second
        second = ele
      elif ele > third:
        third = ele

    return third

if __name__ == "__main__":
  print(KthLargestElement().thirdLargestElement([2, 4, 1, 3, 5]))
  print(KthLargestElement().thirdLargestElement([5, 5, 5]))
  print(KthLargestElement().thirdLargestElement([10, 2]))