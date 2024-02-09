#include <stdio.h>

int calculate(int num1, int num2, char sign)
{
    int greater = (num1 > num2)*num1 + (num2 > num1)*num2 + (num2 == num1)*num1;
    int smaller = (num1 < num2)*num1 + (num2 < num1)*num2 + (num2 == num1)*num1;

    return ('>' == sign)*greater + ('<' == sign)*smaller;
}

// Sort with for loop without if statement
void sortWithForLoop(int arr[], int size)
{
    int i, j;
    int n = size;
    for (i = 0; i < n-1; i++) {
        // Last i elements are already in place, but we'll still go through them
        for (j = 0; j < n-i-1; j++) {
            int greater = calculate(arr[j], arr[j+1], '>');
            int smaller = calculate(arr[j], arr[j+1], '<');

            arr[j] = smaller;
            arr[j+1] = greater; 
        }
    }
}

// Sort with while loop without if statement
void sortWithWhileLoop(int arr[], int size) {
    int i = 0, j;
    int n = size;
    while (i < n - 1) {
        j = 0; // Initialize j for the inner loop
        while (j < n - i - 1) {
            int greater = calculate(arr[j], arr[j + 1], '>');
            int smaller = calculate(arr[j], arr[j + 1], '<');

            arr[j] = smaller;
            arr[j + 1] = greater;

            j++; // Increment j at the end of the inner loop
        }
        i++; // Increment i at the end of the outer loop
    }
}


// sort with if only
void sortArrWithSizeOf5(int arr[])
{
    int smallerIndex = 0, temp;
    
    // loop 5 elements
    if(arr[smallerIndex] > arr[1])
        smallerIndex = 1;
    if(arr[smallerIndex] > arr[2])
        smallerIndex = 2;
    if(arr[smallerIndex] > arr[3])
        smallerIndex = 3;
    if(arr[smallerIndex] > arr[4])
        smallerIndex = 4;
    temp = arr[0];
    arr[0] = arr[smallerIndex];
    arr[smallerIndex] = temp;

    // loop 4 elements
    smallerIndex = 1;
    if(arr[smallerIndex] > arr[2])
        smallerIndex = 2;
    if(arr[smallerIndex] > arr[3])
        smallerIndex = 3;
    if(arr[smallerIndex] > arr[4])
        smallerIndex = 4;
    temp = arr[1];
    arr[1] = arr[smallerIndex];
    arr[smallerIndex] = temp;

    // loop 3 elements
    smallerIndex = 2;
    if(arr[smallerIndex] > arr[3])
        smallerIndex = 3;
    if(arr[smallerIndex] > arr[4])
        smallerIndex = 4;
    temp = arr[2];
    arr[2] = arr[smallerIndex];
    arr[smallerIndex] = temp;

    // loop 2 elements
    smallerIndex = 3;
    if(arr[smallerIndex] > arr[4])
        smallerIndex = 4;
    temp = arr[3];
    arr[3] = arr[smallerIndex];
    arr[smallerIndex] = temp;
}

// sort with goto without loops
void bubbleSortWithGoto(int arr[], int size) {
    int i = 0, j, temp;

    start_outer_loop:
        if (i >= size - 1) goto end_outer_loop; // Exit condition for the outer loop
        j = 0;

    start_inner_loop:
        if (j >= size - i - 1) goto end_inner_loop; // Inner loop exit condition
        if (arr[j] > arr[j + 1]) {
            // Swap the elements
            temp = arr[j];
            arr[j] = arr[j + 1];
            arr[j + 1] = temp;
        }
        j++;
        goto start_inner_loop; // Jump back to the start of the inner loop

    end_inner_loop:
        i++;
        goto start_outer_loop; // Jump back to the start of the outer loop

    end_outer_loop:
        ; // This semicolon is an empty statement, needed because labels must be followed by a statement
}

void printArr(int arr[], int size)
{
    int i = 0;
    printf("Array: \n");
    for (i = 0; i < size; i++) 
    {
       printf("%d, ", arr[i]);
    }
    printf("\n");
}

int main(void)
{
    int arr1[] = {5,20,3,60,10};
    int arr2[] = {5,20,3,60,10};
    int arr3[] = {5,20,3,60,10};
    int arr4[] = {5,20,3,60,10};
    int size = 5;
    sortWithForLoop(arr1,size);
    sortWithWhileLoop(arr2,size);
    sortArrWithSizeOf5(arr3);
    bubbleSortWithGoto(arr4,size);

    printArr(arr1,size);
    printArr(arr2,size);
    printArr(arr3, size);
    printArr(arr4,size);
    return 0;
}
