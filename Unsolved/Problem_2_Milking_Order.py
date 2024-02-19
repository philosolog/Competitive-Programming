n, k = None, None
cl = None
mo = None

with open("milkorder.in", "r") as fin:
	n, m, k = map(int, fin.readline().split())
	cl = list(map(int, fin.readline().split()))[::-1]
	mo = [0 for _ in range(n)]

	for _ in range(k):
		c, p = map(int, fin.readline().split())

		mo[p-1] = c

mo = mo[::-1]
c = 0

for v in cl:
	if v in mo:
		c = mo.index(v)
	else:
		mo[mo.index(0, c)] = v

mo = mo[::-1]

with open("milkorder.out", "w") as fout:
	if 1 in mo:
		fout.write(str(mo.index(1)+1))
	else:
		fout.write(str(mo.index(0)+1))