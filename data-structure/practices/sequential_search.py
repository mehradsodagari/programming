def sequential_search(lst,target):
    if not lst:return 
    position=0 
    while position<len(lst):
        if lst[position]==target:
            return position 
        position+=1 
    return -1 