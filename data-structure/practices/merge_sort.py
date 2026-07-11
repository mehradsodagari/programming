def merge(lst,copy_buffer,low,middle,high):
    i1=low 
    i2=middle+1 
    for i in range(low,high+1):
        if i1>middle:
            copy_buffer[i]=lst[i2]
            i2+=1 
        elif i2>high:
            copy_buffer[i]=lst[i1]
            i1+=1 
        elif lst[i1]<lst[i2]:
            copy_buffer[i]=lst[i1] 
            i1+=1
        else:
            copy_buffer[i]=lst[i2] 
            i2+=1
    for i in range(low,high+1):
        lst[i]=copy_buffer[i] 
def merge_sort_helper(lst,copy_buffer,low,high):
    if low<high:
        middle=(low+high)//2 
        merge_sort_helper(lst,copy_buffer,low,middle)
        merge_sort_helper(lst,copy_buffer,middle+1,high) 
        merge(lst,copy_buffer,low,middle,high)
def merge_sort(lst):
    copy_buffer=[0]*len(lst) 
    merge_sort_helper(lst,copy_buffer,0,len(lst)-1) 
    return lst
print(merge_sort([3,2,4,5,2,65,43,5]))