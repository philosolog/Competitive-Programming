for _ in range(int(input())):
	m = [[j for j in input()] for i in range(3)]
	tr = None

	for r in range(3):
		for c in range(3):
			if m[r][c] == "?":
				tr = [x for x in m[r] if x != "?"]

	print(*set(["A", "B", "C"]).symmetric_difference(set(tr)))

	

	