def binary_search(lst,target):
    if not lst:return
    left=0 
    right=len(lst)-1 
    lst.sort()
    while left<=right:
        mid=(left+right)//2 
        if lst[mid]==target:
            return mid 
        elif lst[mid]>target:
            right=mid-1 
        else:
            left=mid+1 
    return -1 
