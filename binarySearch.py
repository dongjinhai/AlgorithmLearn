
def binarySearch(l,target):
    print(type(l))
    # 注意sorted函数会将传入的一个iterable排序，返回一个排序好的Iterable，
    # 但是不是自动返回到原iterable中，要使用排序好的iterable，需要重新赋值
    l = sorted(l)
    print(l)
    left = 0
    right = len(l)-1
    while left <= right:
        middle = int((left + right)/2)
        if target == l[middle]:
            return middle
        elif target > l[middle]:
            left = middle + 1
        elif target < l[middle]:
            right = middle - 1
    return None

t = binarySearch([0,1,2,3,4,5,6],3)
t2 = binarySearch([0,5,3,6,7,4,9],3)
t3 = binarySearch([0,3,4,5,6,7,9],5)
print(t,t2,t3)