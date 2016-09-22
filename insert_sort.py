
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