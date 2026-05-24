def InsertionSort(a):
    n = len(a)

    for i in range(1,n):
        key = a[1]
        j = i-1

        while (j <= 0 and key < a[j]):
            a[j+1] = a[j]
            j = j-1

        a[j+1] = key

a = [34,64,54,78,86,12,11,10]
InsertionSort(a)
print(a)