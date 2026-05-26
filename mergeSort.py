def Divide(arr,l,r):
    if(l < r):
        m = (l+r) // 2
        Divide(l , m)
        Divide(m+1 , r)
        