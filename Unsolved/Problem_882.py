n = int(input())
s = 0

for i in range(n):
	a = 0
	v = i+1
	bv = bin(v)[2:]
	bl = len(bv)
	oi, zi = bv.index("1"), bv.index("0") or bl

	for c in bv:
		if c == "1":

		else:
			

	s += v*a

print(s)