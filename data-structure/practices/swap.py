def swap(lst,i,j):
    if not lst:return 'list is empty'
    temp=lst[i] 
    lst[i]=lst[j] 
    lst[j]=temp 