class MoveZerosAtEnd:
    def function_BruteForce(self, arr):
        temp = []

        for ele in arr:
            if ele != 0:
                temp.append(ele)
        
        for i in range(len(temp)):
            arr[i] = temp[i]
        
        for i in range(len(temp), len(arr), 1):
            arr[i] = 0

    
    def funtion_OptimalSolution(self, arr):
        # First check for zeroes

        N = len(arr)

        j = -1

        for i in range(N):
            if arr[i] == 0:
                j = i
                break
        
        if j == -1:
            return
        
        
        
        # for i in range(j+1, len(arr)):
        #     if arr[i] != 0:
        #         arr[i], arr[j] = arr[j], arr[i]
        #         j += 1
        i = j+1
        while i < N:
            if arr[i] != 0:
                arr[i], arr[j] = arr[j], arr[i]
                j += 1
            
            i += 1
        

if __name__ == "__main__":
    arr = [2, 0, 0, 4, 5, 0, 1, 0, 3, 0]
    MoveZerosAtEnd().function_BruteForce(arr)
    print(arr)

    arr = [2, 0, 0, 4, 5, 0, 1, 0, 3, 0]
    MoveZerosAtEnd().funtion_OptimalSolution(arr)
    print(arr)