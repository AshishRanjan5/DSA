class SumNNaturalNumber:
  def sumO_N(self, n):
    res = 0
    for i in range(1, n+1):
      res += i
    return res

  def sumO_1(self, n):
    return n*(n+1)//2

if __name__ == "__main__":
  sumN = SumNNaturalNumber()
  print(sumN.sumO_N(5))
  print(sumN.sumO_1(5))