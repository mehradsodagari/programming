def swap(lst,i,j):
    temp=lst[i] 
    lst[i]=lst[j] 
    lst[j]=temp 
def partition(lst,left,right):
    middle=(left+right)//2 
    pivot=lst[middle] 
    lst[middle]=lst[right]
    lst[right]=pivot 
    boundry=left 
    for index in range(left,right):
        if lst[index]<pivot:
            swap(lst,index,boundry)
            boundry+=1 
    swap(lst,boundry,right)
    return boundry 
def quick_sort_helper(lst,left,right):
    if left<right:
        pivot_location=partition(lst,left,right)
        quick_sort_helper(lst,left,pivot_location-1)
        quick_sort_helper(lst,pivot_location+1,right) 
def quick_sort(lst):
    quick_sort_helper(lst,0,len(lst)-1)
    return lst
print(quick_sort([3,2,4,5,2,65,43,5]))