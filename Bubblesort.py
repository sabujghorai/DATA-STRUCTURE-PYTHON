# Write a program to sort a list of integers in ascending order using bubble sort
def BubbleSort(a):
    n = len(a)

    for i in range(n):
        for j in range(0,n-1-i):
            if(a[j] > a[j+1]):
                a[j],a[j+1] = a[j+1],a[j]

a = [75,45,34,23,54,27,87,12,47,99]
BubbleSort(a)
print(a)


# Modify bubble sort to sort the array in descending order.
def Bubblesort(b):
    k = len(b)

    for i in range(k):
        for j in range(0,k-1-i):
            if(b[j] < b[j+1]):
                b[j],b[j+1] = b[j+1],b[j]

b = [11,22,33,44,55,66,77]
Bubblesort(b)
print(b)


# Sort the array and also print the total number of swaps 
def BubbleSort_count(c):
    l = len(c)
    swap_count = 0

    for i in range(l):
        for j in range(0,l-1-i):
            if(c[j]>c[j+1]):
                c[j],c[j+1] = c[j+1],c[j]
                swap_count += 1
    return c, swap_count
    
c = [30,32,34,35,46,41,78,31,98]
sorted_array,swap = BubbleSort_count(c)
print("Sorted array is :",sorted_array)
print("number of swap is :",swap)


# Use bubble sort to sort a list of strings alphabetically.
def BubbleSort(d):
    n = len(d)

    for i in range(n):
        for j in range(0,n-1-i):
            if(d[j] > d[j+1]):
                d[j],d[j+1] = d[j+1],d[j]

d = ["zoo","xmas","string","list","list","tuple","alpha","beta","camel"]
BubbleSort(d)
print(d)
