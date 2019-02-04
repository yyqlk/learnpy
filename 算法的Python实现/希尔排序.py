
def shell_sort(alist):
	n = len(alist)
	gap = n//2
	while gap >= 1:
		for i in range(gap, n):
			while i > 0	and alist[i] < alist[i-gap]:
				alist[i], alist[i-gap] = alist[i- gap], alist[i]
				i -= gap
		gap = gap//2


if __name__ == '__main__':
	alist = [1, 44, 5, 2, 8, 49]
	print(alist)
	shell_sort(alist)
	print(alist)
