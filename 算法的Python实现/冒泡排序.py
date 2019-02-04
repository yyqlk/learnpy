def bubble_sort(alist):
	n = len(alist)
	for j in range(n-1):
		for i in range(n-1-j):
			if alist[i] > alist[i+1]:
				alist[i], alist[i+1] = alist[i+1], alist[i]


if __name__ == '__main__':
	alist = [1, 44, 5, 2, 8, 49]
	print(alist)
	bubble_sort(alist)
	print(alist)


