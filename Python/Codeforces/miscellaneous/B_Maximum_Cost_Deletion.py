for _ in range(int(input())):
	n, a, b = map(int, input().split())
	s = input()
	ns = []

	for i, c in enumerate(s):
		if i != 0:
			if c != s[i-1]:
				ns.append(c)
		else:
			ns.append(c)

	m = len(ns)

	print(a*n + max(b*n, (m//2+1)*b))