import java.util.Arrays;

public class MergeSort {
    private void merge(int[] arr, int left, int mid, int right){

        int[] L = Arrays.copyOfRange(arr, left, mid+1);
        int[] R = Arrays.copyOfRange(arr, mid+1, right+1);
        int i = 0;
        int j = 0;
        int k = left;

        while(i<L.length && j<R.length){
            if(L[i]< R[j]){
                arr[k] = L[i];
                k++;
                i++;
            } 
            else{
                arr[k] = R[j];
                k++;
                j++;
            }
        while(i< L.length){
            arr[k] = L[i];
            i++;
            k++;
        }
        while(j< R.length){
            arr[k] = R[j];
            j++;
            k++;
        }



        }
    }

    public void sortArray(int[] arr, int left, int right){
        if (left >= right){
            return;
        }
        int mid = (int)((left+right)/2);
        sortArray(arr, left, mid);
        sortArray(arr, mid+1, right);
        merge(arr, left, mid, right);

    }
    public static void main(String[] args) {
        MergeSort mergeSort = new MergeSort();
        int[] arr = {2, 4, 1, 3, 5};
        mergeSort.sortArray(arr, 0,  arr.length - 1);

        for(int i=0; i<arr.length; i++){
            System.out.println(arr[i]);
        }
        
    }
    
}
