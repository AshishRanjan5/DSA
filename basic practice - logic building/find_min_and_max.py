class Max_Min:
  def maxMinElement(self, A):
    maxEle = 0
    minEle = float('inf')
    minIndex = 0
    maxIndex = 0

    for index, value in enumerate(A):
      if value>maxEle:
        maxEle = max(maxEle, value)
        maxIndex = index
      if value<minEle:
        minEle = min(minEle, value)
        minIndex = index
    
    return {"minIndex":minIndex, "maxIndex": maxIndex}

if __name__ == "__main__":
  maxMin = Max_Min()
  print(maxMin.maxMinElement([1, 2, 3, 4, 5, 4, 3, 2, 1, 0]))