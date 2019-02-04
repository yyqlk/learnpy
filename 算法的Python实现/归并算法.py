def merge_sort(alist):
	n = len(alist)
	if n <= 1:
		return alist
	mid = n // 2
	# 理解递归，每次返回排序好左右两边，一层一层往上
	left_list = merge_sort(alist[:mid])
	right_list = merge_sort(alist[mid:])
	
	left_pointer, right_pointer = 0, 0
	result = []
	while left_pointer < len(left_list) and right_pointer < len(right_list):
		if left_list[left_pointer] <= right_list[right_pointer]:
			result.append(left_list[left_pointer])
			left_pointer += 1
		else:
			result.append(right_list[right_pointer])
			right_pointer += 1
	result += left_list[left_pointer:]
	result += right_list[right_pointer:]
	return result


if __name__ == '__main__':
	alist = [1, 44, 5, 2, 8, 49]
	print(alist)
	new_alist = merge_sort(alist)
	print(new_alist)





