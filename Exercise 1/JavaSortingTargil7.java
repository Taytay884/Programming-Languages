import java.time.Duration;
import java.time.Instant;
import java.util.Random;

class JavaSortingTargil7 {
    public static void main(String[] args) {
       int[] arr1 = generateRandomArray(10, 0, 10);
       int[] arr2 = generateRandomArray(100, 0, 100);
       int[] arr3 = generateRandomArray(1000, 0, 1000);
       int[] arr4 = generateRandomArray(10000, 0, 10000);

       sortAndTakeTime(arr1);
       sortAndTakeTime(arr2);
       sortAndTakeTime(arr3);
       sortAndTakeTime(arr4);
    }

    public static int[] generateRandomArray(int size, int min, int max) {
        Random rand = new Random();
        int[] array = new int[size];

        for (int i = 0; i < array.length; i++) {
            array[i] = rand.nextInt((max - min) + 1) + min;
        }

        return array;
    }

    public static void sortAndTakeTime(int[] arr){
        long start1 = System.nanoTime();
        bubbleSort(arr);
        long end1 = System.nanoTime();      
        System.out.println("Elapsed Time in nano seconds: "+ (end1-start1));  
    }
    
    // without objects
    public static void bubbleSort(int[] arr) {
        int n = arr.length;
        int temp = 0;
        
        for(int i = 0; i < n; i++) {
            for(int j = 1; j < (n-i); j++) {
                if(arr[j-1] > arr[j]) {
                    // Swap elements
                    temp = arr[j-1];
                    arr[j-1] = arr[j];
                    arr[j] = temp;
                }
            }
        }
    }

    // with objects
    public static void bubbleSort(Number[] arr) {
        int n = arr.length;
        Number temp;
        
        for (int i = 0; i < n; i++) {
            for (int j = 1; j < (n - i); j++) {
                if (arr[j - 1].intValue() > arr[j].intValue()) {
                    // Swap elements
                    temp = arr[j - 1];
                    arr[j - 1] = arr[j];
                    arr[j] = temp;
                }
            }
        }
    }
}