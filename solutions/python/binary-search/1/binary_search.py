def find(search_list, value):
    l=0
    r=len(search_list)-1

    while l<=r:
        m=(l+r)//2
        mid=search_list[m]

        if mid==value:
            return m
        elif mid<value:
            l=m+1
        else:
            r=m-1

    raise ValueError("value not in array")
    