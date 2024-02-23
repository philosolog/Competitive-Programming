import bisect

n, q = map(int, input().split())
cl = [int(x) for x in input().split()]
tl = [int(x) for x in input().split()]
dl = []

for i, c in enumerate(cl):
	d = cl[i]-tl[i]

	if d > 0:
		dl.append(d)
	else:
		n -= 1

dl = sorted(dl)
madl = max(dl)

for _ in range(q):
	v, s = map(int, input().split())

	if s >= madl or v > n-(bisect.bisect(dl, s)):
		print("NO")
		
		continue

	print("YES")