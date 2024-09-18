for a in range(1, 999):
	for b in range(a, 999):
		for c in range(b, 999):
			if a + b + c == 1000 and a * a + b * b == c * c:
				print(a * b * c)
				exit()