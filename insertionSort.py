def insertionSort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

arr = [8, 4, 2, 9, 1, 5]
insertionSort(arr)
print("Sorted array:", arr)

# descending order version 
def insertionSortDescending(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

arr = [8, 4, 2, 9, 1, 5]
insertionSortDescending(arr)
print(arr)