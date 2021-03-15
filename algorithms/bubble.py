import time
import random
                    
def bubble_sort(arr):
    '''
    Sorts the list/array using bubble sort.
    '''
    index = 1
    for _ in range(len(arr) - index):
        for j in range(0, len(arr) - index):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            yield arr 
        index += 1

if __name__ == '__main__':
    arr = [random.randrange(50,100) for i in range(1, 50)]
    arr_check = arr[:]
    arr_check.sort()
    for array in bubble_sort(arr):
        print(array)
        time.sleep(0.000005)
    assert arr == arr_check 