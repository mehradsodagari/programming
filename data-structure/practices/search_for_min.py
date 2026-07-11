def index_of_min(lst):
    if not lst:return 
    min_index=0 
    index=0 
    while index<len(lst):
        if lst[index]<lst[min_index]:
            min_index=index 
        index+=1
    return min_index 