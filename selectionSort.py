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
def ascendingOrderSort(arr):
    n = len(arr)

    for i in range(n):
        min = i
        for j in range(i,n):
            if(arr[min]>arr[j]):
                min  = j
        arr[i],arr[min] = arr[min],arr[i]

arr = [64,25,12,22,11]
ascendingOrderSort(arr)
print(arr)


# sort the elements arr = [5, 9, 1, 3, 7] in descending order
def descendingOrderSort(arr):
    n = len(arr)

    for i in range(n):
        min = i
        for j in range(i,n):
            if(arr[min]<arr[j]):
                min = j
        arr[min],arr[i] = arr[i],arr[min]


arr = []

n = int(input("Wnter how many numbers you want to sort :"))
for k in range(n):
    elements = int(input("Enter the elements :"))
    arr.append(elements)

descendingOrderSort(arr)
print(arr)