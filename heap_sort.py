"""
构建堆的时候，只需要从其1/2处开始，从下往上慢慢构建一个堆
调整堆的时候只需要从顶开始，并且只需要调整交换了值的子树。
排序的时候每次将0位和最后以为调换位置，然后将数组减一，再调整堆。
"""
def heapify(origin_list,start,end):
    flag = 2*start+1
    while flag <= end:
        #判读是否有右孩子，并比较左右孩子大小
        if flag+1<=end and origin_list[flag]<origin_list[flag+1]:
            flag = flag+1
        if origin_list[start]<origin_list[flag]:
            origin_list[start],origin_list[flag]=origin_list[flag],origin_list[start]
        start = flag
        flag = 2*start+1
    return origin_list

def heapSort(origin_list):
    #构建堆
    for i in range(len(origin_list)//2-1,-1,-1):
        origin_list = heapify(origin_list,i,len(origin_list)-1)
    #排序
    for i in range(len(origin_list)-1,-1,-1):
        origin_list[0],origin_list[i]=origin_list[i],origin_list[0]
        origin_list = heapify(origin_list,0,i-1)
    return origin_list

origin_list = [1,5,8,4,6,9,7,45,56,23,78,49,646]
print(heapSort(origin_list))


"""
heapify函数调整堆，一边之后将最大的那个数变成根
heapSort，每次将最大的那个数移到后面
"""
#以下代码错误，可以实现排序，不符合堆排序思想，时间复杂度为O(n**2)，而堆排序时间复杂度为O(nlogn)
def error_heapify(origin_list,n):
    t = n - 1
    for i in range(n-1,-1,-1):
        if i == 0:
            break
        if origin_list[i]>origin_list[i%2+i//2-1]:
            origin_list[i],origin_list[i%2+i//2-1]=origin_list[i%2+i//2-1],origin_list[i]
    return origin_list

def error_heapSort(origin_list):
    origin_list = error_heapify(origin_list,len(origin_list))
    for i in range(len(origin_list)-1,-1,-1):
        origin_list[0],origin_list[i] = origin_list[i],origin_list[0]
        origin_list = error_heapify(origin_list,i)
    return origin_list

origin_list = [1,5,8,6,4,9,45,58,56,89]
print(error_heapSort(origin_list))


