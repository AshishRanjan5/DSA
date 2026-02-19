class MaximumConsecutiveOnes:
    def consecutive(self, arr):
        maxCount = float('-inf')
        countOnes = 0
        for ele in arr:
            if ele == 1:
                countOnes += 1
                maxCount = max(maxCount, countOnes)
            else:
                countOnes = 0

        return maxCount


if __name__ == "__main__":
    arr = [1,1,0,1,1,1,0,1,1,1]
    print(MaximumConsecutiveOnes().consecutive(arr))