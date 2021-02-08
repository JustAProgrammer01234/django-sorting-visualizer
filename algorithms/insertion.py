import time
import random 

def insertion_sort(arr): 
    '''
    Sorts the array using 
    insertion sort
    '''
    for i in range(1, len(arr)):
        char = arr[i]
        j = i - 1
        while j >= 0 and char < arr[j]:
            arr[j + 1] = arr[j]
            j -=1
            yield arr
        arr[j + 1] = char  

#[14,7,4,2,5,7,9]
if __name__ == '__main__':
    arr = [random.randrange(50,100) for i in range(1, 50)]
    print(arr)
    print('')
    arr_check = arr[:]
    arr_check.sort()
    for array in insertion_sort(arr):
        time.sleep(0.0005)
        print(array)
    assert arr == arr_check