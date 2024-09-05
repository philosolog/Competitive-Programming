t = 0

def F(A, B, C):
	l = [A, B, C]
	s = 0

	if len(set(l)) == 2:
		s = 3
	else:
		if B > A:
			s = 5
		else:
			s = 6

	print(s)
	
	return s

for i in range(1, 8):
	for j in range(1, 20):
		print([i**j, j**i, i**j + j**i])
		t += F(i**j, j**i, i**j + j**i)

print(t)