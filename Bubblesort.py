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