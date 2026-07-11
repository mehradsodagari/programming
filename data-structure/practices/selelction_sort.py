def swap(lst,i,j):
    temp=lst[i] 
    lst[i]=lst[j] 
    lst[j]=temp 
def selection_sort(lst):
    i=0 
    while i<len(lst)-1:
        min_index=i 
        j=i+1 
        while j<len(lst):
            if lst[j]<lst[min_index]:
                min_index=j 
            j+=1 
        if min_index!=i:
            swap(lst,min_index,i) 
        i+=1 
    return lst 
