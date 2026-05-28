def QuickSort(arr,l,r):
    if (l < r):
        p = partition(arr,l,r)

        QuickSort(arr,l,p-1)
        QuickSort(arr,p+1,r)


def partition(arr,l,r):
    pivot = arr[l]

    i = l+1
    j = r

    while True:
        while(l < r and arr[i] < pivot):
            i = i + 1

        while(l < r and arr[j] > pivot):
            j = j-1

        if (i < j):
            arr[i],arr[j] = arr[j],arr[i]
        else:
            break
    
    arr[l],arr[j] = arr[j],arr[l]
    return j

arr = [23,45,21,12,11,0,17]
QuickSort(arr,0,len(arr)-1)
print(arr)