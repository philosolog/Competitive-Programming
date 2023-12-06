import math

n, m = [int(x) for x in input().split()]
next = math.ceil((n+1)//2/m)*m

if next <= n:
	print(next)
else:
	print(-1)