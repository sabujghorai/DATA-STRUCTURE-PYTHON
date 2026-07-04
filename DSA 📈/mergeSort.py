def Divide(arr,l,r):
    if(l < r):
        m = (l+r) // 2
        Divide(arr , l , m)#   -----------|
        Divide(arr , m+1 , r)  # ----|----|
        Merge(arr , l , m , r)  #    |    |
                               #     |    |
def Merge(arr , l , m , r):    #     |    |
    s1 = m - l +1  # ________________|    |
    s2 =  r - m    # _____________________|

    L = [0] * s1
    R = [0] * s2

    for i in range(s1): # runs from 0 to s1 size
        L[i] = arr[l+i] # starts from left array and copy from original array(s1)

    for j in range(s2): # runs from 0 to s2
        R[j] = arr[m+1+j] # starts from left array(m+1) and ends copy from original array(s2)

    i = j = 0
    k = l

    while( i < s1 and j < s2):
        if(L[i] < R[j]):
            arr[k] = L[i]
            i = i+1
            k = k+1
        else:
            arr[k] = R[j]
            j = j+1
            k = k+1

    while(i < s1):
        arr[k] = L[i]
        i = i+1
        k = k+1

    while(j < s2):
        arr[k] = R[j]
        j = j+1
        k = k+1

arr = [24,64,11,10,45,34,67,86,23,16]
Divide(arr , 0 , len(arr)-1)
print(arr)


# Sort the array arr = [8,3,5,4,7,6,1,2] using Merge Sort. 
