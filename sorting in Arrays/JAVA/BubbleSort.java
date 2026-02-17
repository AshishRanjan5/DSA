public class BubbleSort {
    public void sortArray(int[] arr){
        for(int i = 0; i < arr.length; i++){
            for(int j = 0; j < arr.length - i - 1; j++){
                if(arr[j] > arr[j+1]){ /*arr[j]<arr[i] for descending order*/
                    int temp = arr[j+1];
                    arr[j+1] = arr[j];
                    arr[j] = temp;

                }
            }
        }
    }
    public static void main(String[] args) {
        BubbleSort bubbleSort = new BubbleSort();
        
        int[] arr = {2, 4, 1, 3, 5};
        bubbleSort.sortArray(arr);

        for(int i=0; i< arr.length; i++){
            System.out.println(arr[i]);
        }
        
    }
}
