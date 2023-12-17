n, k = [int(x) for x in input().split()]

for t in range(n):
	u, s = [int(x) for x in input().split()]

	print(u//(k*s+1)+u%(k*s+1))