for _ in range(int(input())):
	l = [int(x) for x in input().split()]
	h = []

	for i in l:
		if i not in h:
			h.append(i)
		else:
			h.remove(i)
	
	print(*h)