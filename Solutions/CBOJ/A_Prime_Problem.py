for _ in range(int(input())):
	a, b = map(int, input().split())
	l = [True for _ in range(b+1)]
	l[0] = False

	for i, v in enumerate(l):
		if v == True:
			c = 2*(i+1)-1

			while c <= b:
				l[c] = False
				
				c += i + 1
	
	print(l[a-1:len(l)-1].count(True))

	# !: TLE