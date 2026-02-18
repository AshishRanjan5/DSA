class LeftRotate:
    
    def reverse(self, arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    def rotateLeftOne(self, arr):
        return arr[1:] + arr[:1]
    
    def rotateLeftOne_2(self, arr):
        N = len(arr)
        firstEle = arr[0]
        for i in range(1, N):
            arr[i-1] = arr[i]
        arr[N-1] = firstEle

    def rotateLeftK_Times(self, arr, K):
        N = len(arr)

        if N == 0:
            return
        
        K = K%N

        if K == 0:
            return

        self.reverse(arr, 0, K-1)
        self.reverse(arr, K, N-1)
        self.reverse(arr, 0, N-1)


if __name__ == "__main__":
    arr = [2, 4, 5, 1, 3]
    print(LeftRotate().rotateLeftOne(arr)) # This does not modify the actual array
    
    arr = [2, 4, 5, 1, 3]
    LeftRotate().rotateLeftOne_2(arr) # modifies the actual array
    print(arr)

    arr = [2, 4, 5, 1, 3]
    LeftRotate().rotateLeftK_Times(arr, 1) # modifies the actual array
    print(arr)