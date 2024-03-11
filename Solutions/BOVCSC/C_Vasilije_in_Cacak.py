for t in range(int(input())):
	n, k, x = [int(x) for x in input().split()]

	bs = k/2*(1+k)
	ts = k/2*(2*n-k+1)

	if x <= ts:
		if x >= bs:
			print("YES")
		else:
			print("NO")
	else:
		print("NO")