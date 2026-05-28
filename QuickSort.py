def QuickSort(arr,l,r):
    if (l < r):
        p = partition(arr,l,r)

    QuickSort(arr,l,p-1)
    QuickSort(arr,l,p+1)


def partition(arr,l,r):
    pivot = arr[l]

    i = l+1
    j = r