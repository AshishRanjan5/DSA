class LeftRotate:
    def rotateOne(self, arr):
        return arr[1:] + arr[:1]
    
    def rotateOne_2(self, arr):
        N = len(arr)
        firstEle = arr[0]
        for i in range(1, N):
            arr[i-1] = arr[i]
        arr[N-1] = firstEle

    
        

if __name__ == "__main__":
    arr = [2, 4, 5, 1, 3]
    print(LeftRotate().rotateOne(arr)) # This does not modify the actual array
    
    arr = [2, 4, 5, 1, 3]
    LeftRotate().rotateOne_2(arr) # modifies the actual array
    print(arr)