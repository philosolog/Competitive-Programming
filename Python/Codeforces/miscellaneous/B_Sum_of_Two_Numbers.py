for t in range(int(input())):
	n = int(input())
	d = [int(x) for x in [*str(n)]]
	x = []
	y = []
	o = 0

	for i, c in enumerate(d):
		if c%2 == 0:
			x.append(str(c//2))
			y.append(str(c//2))
		else:
			x.append(str((c+(-1)**o)//2))
			y.append(str((c+(-1)**(o+1))//2))

			o += 1
	
	print(str(int("".join(x))) + " " + str(int("".join(y))))