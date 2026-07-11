def insertion_sort(lst):
    i=1 
    while i<len(lst):
        item_to_index=lst[i] 
        j=i-1 
        while j>=0:
            if item_to_index>lst[j]:
                lst[j+1]=lst[j] 
                j-=1 
            else:
                break 
        lst[j+1]=item_to_index 
        i+=1 
    return lst 