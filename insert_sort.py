
def order_in(list,item):
	if len(list)==0:
		list.append(item)
	else:
		for i in range(len(list)-1,-1,-1):
			if item > list[i]:
				list.insert(i+1,item)
				break
			if i == 0:
				list.insert(0,item)

def insertSort(originList):
	if len(originList) == 0 or len(originList) == 1:
		return originList
	sorted_list = []
	for item in originList:
		order_in(sorted_list,item)
	return sorted_list

originList = [1,5,2,3,6,4,5,8,7,9,4,4,5,5,6,6,12,45,78]
print(insertSort(originList))
originList = [1,4,2,6,8,7,9,45,56,78,45]
print(insertSort(originList))
originList = []
print(insertSort(originList))
originList = [3,2]
print(insertSort(originList))
originList = [1]
print(insertSort(originList))


def insert_sort(lst):
    if len(lst) == 0 or len(lst) == 1:
        return lst
    else:
        tmp = []
        for i in lst:
            order_in(tmp, i)
            # print(tmp)
        return tmp


def order_in(lst, item):
    if len(lst) == 0:
        lst.append(item)
    else:
        for i in range(len(lst)):
            print(lst)
            if lst[i] > item:
                lst.insert(i, item)
                break
            if i == len(lst)-1:
                lst.append(item)


ll = [4, 7, 3, 88, 452, 463]
print(insert_sort(ll))
