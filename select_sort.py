
def selectSort(origin_list):
	for i in range(len(origin_list)):
		for j in range(i+1,len(origin_list)):
			if origin_list[i] > origin_list[j]:
				origin_list[i],origin_list[j] = origin_list[j],origin_list[i]
	return origin_list

origin_list = [1,5,8,6,4,9,7,0]
print(selectSort(origin_list))
