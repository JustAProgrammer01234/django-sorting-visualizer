import time 
import random
                    
def bubble_sort(arr):
    '''
    Sorts the list/array using bubble sort.
    '''
    for i in range(len(arr) - 1):
        for j in range(0, len(arr)- i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            yield arr 

if __name__ == '__main__':
    arr = [random.randrange(50,100) for i in range(1, 30)]
    arr_check = arr[:]
    arr_check.sort()
    for array in bubble_sort(arr):
        print(array)
        time.sleep(0.005)
    assert arr == arr_check 

import numpy
