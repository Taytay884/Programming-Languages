#import gc
#gc.disable()

import time
import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                # Swap if the element found is greater than the next element
                arr[j], arr[j+1] = arr[j+1], arr[j]

def generate_random_array(size, min_value, max_value):
    return [random.randint(min_value, max_value) for _ in range(size)]


arr1 = generate_random_array(10, 0, 10)
arr2 = generate_random_array(100, 0, 100)
arr3 = generate_random_array(1000, 0, 1000)
arr4 = generate_random_array(10000, 0, 10000)


start = time.time()
bubble_sort(arr1)
end = time.time()
print("Time took to sort array with", len(arr1) ,"elements is:", end - start)

start = time.time()
bubble_sort(arr2)
end = time.time()
print("Time took to sort array with", len(arr2) ,"elements is:", end - start)

start = time.time()
bubble_sort(arr3)
end = time.time()
print("Time took to sort array with", len(arr3) ,"elements is:", end - start)

start = time.time()
bubble_sort(arr4)
end = time.time()
print("Time took to sort array with", len(arr4) ,"elements is:", end - start)
