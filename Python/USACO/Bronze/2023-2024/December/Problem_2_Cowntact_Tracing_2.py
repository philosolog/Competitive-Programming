from itertools import groupby

cn = int(input())
os = input()
igs = [''.join(g) for k, g in groupby(os) if k == '1']
md = 0
oi = 0

for i, g in enumerate(igs):
	to = len(g)

	if to%2 != 0 or ((g[0] == 1 and i == 0) or (g[-1] == 1 and i == len(igs-1))):
		md = to//2
	else:
		md = (to-1)//2

if md == 0:
	print(os.count('1'))
else:
	for i, g in enumerate(igs):
		to = len(g)

		oi += to-2*md

	print(oi)