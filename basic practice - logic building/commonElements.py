class CommonElement:
  def allCommonElements(self, A, B):
    res = []
    for i in range(len(A)):
      if A[i] in B:
        res.append(A[i])
    return res
  
  def optimizedCommonElements(self, A, B):
    iA = 0
    iB = 0
    lenA = len(A)
    lenB = len(B)
    res = []
    
    while iA < lenA and iB < lenB:
      if A[iA] < B[iB]:
        iA += 1
      elif A[iA] > B[iB]:
        iB += 1
      else:
        res.append(A[iA])
        iA += 1
        iB += 1
     
    return res

if __name__ == "__main__":
  print(CommonElement().allCommonElements([1, 2, 3], [3, 4, 5]))
  print(CommonElement().optimizedCommonElements([1,2,3,4,5], [4,5,6]))
