# Naive solution (doesn't pass the last bonus case)

import copy

for t in range(int(input())):
	h, w, d = [int(x) for x in input().split()]
	tb = h + d + 1
	lr = w + d + 1
	oi = []

	def o(l, v):
		return [int(x) for x, c in enumerate(l) if c == v]
	
	for r in range(h):
		oi.append([*input()]+[" "]*(d+1))
	for r in range(d+1):
		oi.append([" "]*lr)

	ni = copy.deepcopy(oi)
	
	for r in range(tb):
		for co in o(oi[r], "+"):
			for e in range(d):
				ni[r+e+1][co+e+1] = "\\"
	for r in range(h):
		for c in range(w):
			if oi[r][c] != " ":
				ni[r+d+1][c+d+1] = oi[r][c]
	for r in range(tb):
		print("".join(ni[r]))