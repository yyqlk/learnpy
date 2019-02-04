def select_sort(alist):
	n = len(alist)
	for min_pointer in range(n-1):
		for i in range(min_pointer+1, n):
			if alist[min_pointer] > alist[i]:
				alist[min_pointer], alist[i] = alist[i], alist[min_pointer]

	
if __name__ == '__main__':
	alist = [1, 44, 5, 2, 8, 49]
	print(alist)
	select_sort(alist)
	print(alist)	
