
#include <stdio.h>
#include <time.h>
#include <stdlib.h>

int* generate_random_array(int size, int min_value, int max_value) {
    int* array = (int*)malloc(size * sizeof(int)); // Allocate memory for the array
    if (array == NULL) {
        perror("Memory allocation failed");
        exit(EXIT_FAILURE); // Exit if memory allocation fails
    }
    
    for (int i = 0; i < size; i++) {
        // Generate random numbers in [min_value, max_value] range
        array[i] = min_value + rand() % (max_value - min_value + 1);
    }

    return array;
}

void bubbleSort(int arr[], int n) {
    int i, j, temp;
    for (i = 0; i < n-1; i++) {     
        // Last i elements are already in place
        for (j = 0; j < n-i-1; j++) {
            if (arr[j] > arr[j+1]) {
                // Swap arr[j] and arr[j+1]
                temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
            }
        }
    }
}


int main(void)
{
    int size1 = 10;
    int size2 = 100;
    int size3 = 1000;
    int size4 = 10000;
    int *arr1;
    int *arr2;
    int *arr3;
    int *arr4;
    
    arr1 = generate_random_array(size1, 0, size1);
    arr2 = generate_random_array(size2, 0, size2);
    arr3 = generate_random_array(size3, 0, size3);
    arr4 = generate_random_array(size4, 0, size4);

    int i = 0;
    double time_taken = 0;
    clock_t t1;
    clock_t t2;
    clock_t t3;
    clock_t t4;
    //arr1
    t1 = clock();
    bubbleSort(arr1, size1);
    t1 = clock() - t1;
    time_taken = ((double)t1)/CLOCKS_PER_SEC; // calculate the elapsed time
    printf("The sorting for %d elements took %f seconds to execute\n", size1, time_taken);
    
    
    //arr2
    t2 = clock();
    bubbleSort(arr2, size2);
    t2 = clock() - t2;
    time_taken = ((double)t2)/CLOCKS_PER_SEC; // calculate the elapsed time
    printf("The sorting for %d elements took %f seconds to execute\n", size2, time_taken);

    //arr3
    t3 = clock();
    bubbleSort(arr3, size3);
    t3 = clock() - t3;
    time_taken = ((double)t3)/CLOCKS_PER_SEC; // calculate the elapsed time
    printf("The sorting for %d elements took %f seconds to execute\n", size3, time_taken);

    //arr4
    t4 = clock();
    bubbleSort(arr4, size4);
    t4 = clock() - t4;
    time_taken = ((double)t4)/CLOCKS_PER_SEC; // calculate the elapsed time
    printf("The sorting for %d elements took %f seconds to execute\n", size4, time_taken);  
    

    return 0;
}
