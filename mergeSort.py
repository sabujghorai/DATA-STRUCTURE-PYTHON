def Divide(arr,l,r):
    if(l < r):
        m = (l+r) // 2
        Divide(l , m)#   ------------|
        Divide(m+1 , r)  # ----------|----|
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
        R[0] = arr[m+1+j] # starts from left array(m+1) and ends copy from original array(s2)

    i = j = 0
    k = l

    while( i < s1 and j < s2):
        if(l[i] < R[j]):
            arr[k] = R[j]
        
        else:
            arr[k] = R[j]
            j = j+1
            k = k+1