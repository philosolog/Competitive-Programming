import math

for i in range(int(input())):
	n = int(input())
	p = [int(x) for x in input().split()]
	c = 0

	for v in range(n):
		if p[v] == v+1:
			c += 1

	print(math.ceil(c/2))