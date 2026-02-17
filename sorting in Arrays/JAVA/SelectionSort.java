public class SelectionSort
{
    public void sortArray(int arr[])
    {
        for(int i = 0; i < arr.length; i++)
            {
                int minValue = arr[i];
                int minIndex = i;

                for (int j = i+1; j < arr.length; j++)
                {
                    if(arr[j]<minValue)
                    {
                        minValue = arr[j];
                        minIndex = j;
                    }

                }
                int temp = arr[i];
                arr[i] = minValue;
                arr[minIndex] = temp;

            }
    }
    public static void main(String[] args) {
    SelectionSort selectionSort = new SelectionSort();

        int[] arr = {2, 4, 1, 3, 5};   // correct array declaration
        selectionSort.sortArray(arr);

        // print result
        for (int num : arr) {
            System.out.print(num + " ");
        }

        
    }
}



