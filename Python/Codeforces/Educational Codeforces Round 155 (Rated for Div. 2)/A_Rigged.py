for t in range(int(input())):
	trc = []
	c1 = None

	for c in range(int(input())):
		s, e = [int(x) for x in input().split()]

		if c == 0:
			c1 = (s, e)
		else:
			if s >= c1[0]:
				trc.append((s, e))

	tv = c1[0] - 1

	for rc in trc:
		s = rc[0]
		e = rc[1]

		if e >= c1[1]:
			tv = -1
	
	print(tv)
	