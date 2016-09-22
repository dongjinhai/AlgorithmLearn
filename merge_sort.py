
def mergeSort(origin_list):
	if len(origin_list)<=1:
		return origin_list
	middle = len(origin_list)//2
	left = mergeSort(origin_list[:middle])
	right = mergeSort(origin_list[middle:])
	return merge(left,right)

def merge(left,right):
	le,ri = 0,0
	result = []
	while(le<len(left) and ri<len(right)):
		if left[le] < right[ri]:
			result.append(left[le])
			le+=1
		else:
			result.append(right[ri])
			ri+=1
	result += left[le:]
	result += right[ri:]
	return result

origin_list = [1,5,8,6,4,7,9,45,78,546,84961]

print(mergeSort(origin_list))