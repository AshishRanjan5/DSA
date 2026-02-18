#T_N_S_N => time complexity N and space complexity N
#T_N_S_1 => time complexity N and space complexity N


class RemoveDuplicates:
    def removeDuplicatesT_N_S_N(self, arr): #
        res = [arr[0]]

        for i in range(1, len(arr)):
            if arr[i] != arr[i-1]:
                res.append(arr[i])
        
        return res
    
    def removeDuplicatesT_N_S_N_w_Set(self, arr):
        s = set()
        for ele in arr:
            s.add(ele)
        i = 0
        for ele in s:
            arr[i] = ele
            i += 1

        return arr[:i]

    def removeDuplicatesT_N_S_1(self, arr):
        i = 0
        j = 1
        while j < len(arr):
            if arr[i] != arr[j]:
                 arr[i+1] = arr[j]
                 i += 1
            
            j += 1
        
        return arr[:i+1]


    
if __name__ == "__main__":
    arr = [1, 1, 1, 2, 3, 3, 4, 5, 5]
    print(RemoveDuplicates().removeDuplicatesT_N_S_N(arr))
    arr = [1, 1, 1, 2, 3, 3, 4, 5, 5]
    print(RemoveDuplicates().removeDuplicatesT_N_S_N_w_Set(arr))
    arr = [1, 1, 1, 2, 3, 3, 4, 5, 5]
    print(RemoveDuplicates().removeDuplicatesT_N_S_1(arr))