def selectionSort(a):
    n = len(a)

    for i in range (n):
        min = i
        for j in range (i , n):
            if(a[min]>a[j]):
                min = j
        a[i],a[min] = a[min],a[i]
    
a = [65,70,72,56,15,67,89]
selectionSort(a)
print(a)


# sort the elements arr = [64,25,12,22,11] in ascending order
def ascendingOrderSort(a):
    n = len(a)

    for i in range(n):
        min = i
        for j in range(i,n):
            if(a[min]>a[j]):
                min  = j
                