class UnionList:
  def unionList(self, A, B):
    return list(set(A).union(set(B)))


if __name__ == "__main__":
  union_list = UnionList()
  print(union_list.unionList([1,2,3], [3,4,5]))