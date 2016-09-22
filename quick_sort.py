
def partition(inlist,begin,end):
	baseValue = inlist[begin]
	baseKey = begin
	while(begin<end):
		while(begin<end and inlist[end]>=baseValue):
			end -= 1
		inlist[begin],inlist[end] = inlist[end],inlist[begin]
		baseKey = end
		while(begin<end and inlist[begin]<=baseValue):
			begin += 1
		inlist[begin],inlist[end] = inlist[end],inlist[begin]
		baseKey = begin
	return baseKey

def quickSort(inlist,begin,end):
	if(begin<end):
		pivotloc = partition(inlist,begin,end)
		quickSort(inlist,begin,pivotloc-1)
		quickSort(inlist,pivotloc+1,end)
	return inlist

origin_list = [1,5,6,8,5,15,6,9,78,46,56,23,45,9,75]

print(quickSort(origin_list,0,len(origin_list)-1))