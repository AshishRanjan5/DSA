class MergeSort:

    def merge(self, arr, left, mid, right):
        # create temp arrays
        L = arr[left:mid+1]
        R = arr[mid+1:right+1]

        i = 0
        j = 0
        k = left

        # merge
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # remaining elements
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    def sortArray(self, arr, left, right):
        if left >= right:      # base condition
            return

        mid = (left + right) // 2

        self.sortArray(arr, left, mid)
        self.sortArray(arr, mid + 1, right)
        self.merge(arr, left, mid, right)

if __name__ == "__main__":
    arr = [2, 4, 1, 3, 5]
    MergeSort().sortArray(arr, 0, len(arr)-1)
    print(arr)