
def bub_sort(list):
	index = 1
	while(index <= len(list)):
		for i in range(len(list)-index):
			if list[i] > list[i+1]:
				temp = list[i]
				list[i] = list[i+1]
				list[i+1] = temp
		index += 1
	return list
inlist = [1,5,6,2,7,8,4,3]
relist = bub_sort(inlist)
print(relist)

