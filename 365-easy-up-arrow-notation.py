def uparrow(num, times, n_arrow):
	res = num
	if n_arrow == 1:
		return num ** times
	else:
		for i in range(times - 1):
			res = uparrow(num, res, n_arrow-1)
	return res

print(uparrow(2, 4, 1))
print(uparrow(2, 3, 3))
