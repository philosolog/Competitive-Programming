for _ in range(int(input())):
	n = int(input())
	s = input()
	vl = ["a", "e"]
	cl = ["b", "c", "d"]
	ns = []
	nns = []

	for i, ch in enumerate(s):
		if i > 2:
			if ch in cl and ns[-1] in vl and ns[-2] in cl and ns[-3] in vl:
				on1 = ns[-1]
				on2 = ns[-2]
				del ns[-1]
				del ns[-1]
				ns.extend([".", on2, on1, ch])
			else:
				ns.append(ch)
		else:
			ns.append(ch)
	for i, ch in enumerate(ns):
		if i > 0 and i != n-1:
			if (ch in cl and ns[i-1] in cl) or (ch in cl and ns[i-1] in vl):
				nns.extend([".", ch])
			else:
				nns.append(ch)
		else:
			nns.append(ch)
	
	print("".join(nns))