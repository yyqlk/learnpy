

def quick_sort(alist, first, last):
	if first >= last: # 只有全部分割成一个元素的，我们就返回，否则一直分割，容易出错的地方就是没有把大于考虑进去，我们只要不存在first<last就停止
		return
	mid_value = alist[first]
	low = first
	high = last
	while low < high:
		while low < high and alist[high] >= mid_value:
			high -= 1
		alist[low] = alist[high]
		while low < high and alist[low] < mid_value:
			low += 1				
		alist[high] = alist[low]
	alist[low] = mid_value 
	quick_sort(alist, first, low-1)
	quick_sort(alist, low+1, last)

if __name__ == '__main__':
	alist = [7, 44, 5, 2, 8, 49]
	print(alist)
	quick_sort(alist, 0, len(alist)-1)
	print(alist)


