"""
增量选择：没有除1之外的公因子，且最后一个增量为1.
"""
def shellSort(origin_list):
 	for incr in [9,5,3,2,1]:
 		for i in range(len(origin_list)):
 			if i+incr >= len(origin_list):
 				if origin_list[i] > origin_list[-1]:
 					origin_list[i],origin_list[-1]=origin_list[-1],origin_list[i]
 			else:
 				if origin_list[i] > origin_list[i+incr]:
 					origin_list[i],origin_list[i+incr]=origin_list[i+incr],origin_list[i]
 	return origin_list

origin_list = [1,5,8,9,6,45,78,95,53,64,84]
print(shellSort(origin_list))