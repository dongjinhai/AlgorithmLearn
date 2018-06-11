
"""选择排序是每次将最小（大）的元素找出来，和查找列表的最左（右）的元素交换值
和冒泡排序的区别是冒泡排序一趟中可能要交换几次元素。
选择排序在一趟排序中只是记录最大最小元素的位置，最后再交换元素
"""

def select_sort(lst):
	for i in range(len(lst)):
		min = lst[i]
		index = i
		for j in range(i+1, len(lst)):
			if min > lst[j]:
				min = lst[j]
				index = j
		lst[i], lst[index] = lst[index], lst[i]
	return lst

origin_list = [1,5,8,6,4,9,7,0]
print(selectSort(origin_list))
