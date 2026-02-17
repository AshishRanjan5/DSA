public class InsertionSort {
    public void sortArray(int[] arr){
        for(int i = 1; i < arr.length; i++){
            int key = arr[i];
            int j = i - 1;

            while(j >= 0 && arr[j] > key){
                arr[j + 1] = arr[j];   // shift right
                j--;
            }

            arr[j + 1] = key;          // insert
        }
    }

    public static void main(String[] args) {
        InsertionSort insertionSort = new InsertionSort();
        int[] arr = {2, 4, 1, 3, 5};
        insertionSort.sortArray(arr);

        for(int i=0; i<arr.length; i++){
            System.out.println(arr[i]);
        }
    }
    
}
