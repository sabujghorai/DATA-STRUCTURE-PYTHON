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
    