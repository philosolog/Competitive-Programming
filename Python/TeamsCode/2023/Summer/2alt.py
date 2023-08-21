for t in range(int(input())):
	n = int(input())
	p = [int(x) for x in input().split()]
	p.reverse()

	c = 0

	for i in range(n):
		if p[i] != n-i:
			c += 1
	
	print(c)