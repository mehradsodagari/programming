def swap(lst,i,j):
    temp=lst[i] 
    lst[i]=lst[j] 
    lst[j]=temp 
def bubble_sort(lst):
    n=len(lst) 
    while n>1:
        i=1 
        swapped=False 
        while i<n:
            if lst[i]<lst[i-1]:
                swap(lst,i,i-1) 
                swapped=True 
            i+=1 
        if not swapped:return 
        n-=1 
    return lst 