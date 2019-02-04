def insert_sort(alist):
	n = len(alist)
	for i in range(1, n):
		# while i > 0:
		# 	if alist[i] < alist[i-1]:
		while i > 0 and alist[i] < alist[i-1]:
			alist[i], alist[i-1] = alist[i-1], alist[i]
			i -= 1
			# else:
			# 	break

if __name__ == '__main__':
	alist = [1, 44, 5, 2, 8, 49]
	print(alist)
	insert_sort(alist)
	print(alist)