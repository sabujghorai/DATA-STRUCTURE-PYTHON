def find_min_max(arr ,start , end):
    if(start == end ):
        return arr[start] , arr[end]

    if(start+1 == end):
        if(arr[start]<arr[end]):
            return arr[start] , arr[end]
        else:
            return arr[end] , arr[start]
        