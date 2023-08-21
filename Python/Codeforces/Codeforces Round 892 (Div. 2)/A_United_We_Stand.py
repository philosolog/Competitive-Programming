for test in range(int(input())):
	n = int(input())
	a = [int(x) for x in input().split()]

	a.sort()

	if len(set(a)) == 1:
		print(-1)
	else:
		fc = a.count(a[0])

		print(fc, n-fc)
		print(*a[:fc])
		print(*a[fc:])