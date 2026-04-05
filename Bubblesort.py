def BubbleSort(a):
    n = len(a)

    for i in range(n):
        for j in range(0,n-1-i):
            if(a[j] > a[j+1]):
                a[j],a[j+1] = a[j+1],a[j]

a = [75,45,34,23,54,27,87,12,47,99]
BubbleSort(a)
print(a)