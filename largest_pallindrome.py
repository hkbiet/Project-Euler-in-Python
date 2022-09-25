def dual_pallindrome():
	largest_pallindrome = 0
	for i in range(100, 1000):
		for j in range(100, 1000):
			product = i * j
			if (is_pallindrome(product)) and product > largest_pallindrome:
				largest_pallindrome = product
	return largest_pallindrome



def is_pallindrome(num_string):
	num_string_list = list(str(num_string))
	left  = 0
	right = len(num_string_list) - 1

	while left <= right :
		if num_string_list[left] != num_string_list[right]:
			return 0
		left +=1
		right -=1
	if num_string_list[left] == num_string_list[right]:
		return 1
	else:
		return 0

if __name__ == "__main__":
	largest_pallindrome = dual_pallindrome()
	print("LARGEST DUAL PALLINDROME : ", largest_pallindrome)

