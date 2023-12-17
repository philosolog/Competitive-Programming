for t in range(int(input())):
	n = int(input())
	mc = [int(x) for x in input().split()]
	o = mc[0]
	
	for an in range(n-1):
		a = [int(x) for x in input().split()]
		if a[0] >= mc[0] and a[1] >= mc[1]:
			o = -1

	print(o)