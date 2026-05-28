def QuickSort(arr,l,r):
    if (l < r):
        p = partition(arr,l,r)

    QuickSort(arr,l,p-1)
    QuickSort(arr,l,p+1)


def partition(arr,l,r):
    pivot = arr[l]

    i = l+1
    j = r

    while True:
        while(l < r and arr[i] < pivot):
            i = i + 1

        while(l < r and arr[j] > pivot):
            j = j-1