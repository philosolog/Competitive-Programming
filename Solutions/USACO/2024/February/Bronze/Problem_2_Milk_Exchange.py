def main():
	n, m = map(int, input().split())
	o = input()
	ol = [1]*n
	clm = [int(x) for x in input().split()]
	cl = [x for x in clm]
	rl = [-1]*n
	ch = []
	
	def uc(i, c, t):
		cl[i] = min(max(c+t*rl[i], 0), clm[i])
	def ur(i):
		if i not in ch and cl[i] == 0:
			rl[(i+ol[i]+1)%n-1] -= 1

			ch.append(i)

	for i, c in enumerate(o):
		if c == "R":
			rl[(i+1+1)%n-1] += 1
		elif c == "L":
			ol[i] = -1

			rl[(i-1+1)%n-1] += 1

	if len(set(o)) == 1:
		print(sum(cl))

		return

	while m > 0:
		t = max(min(min(cl), m), 1)
		
		if max(cl) != 0:
			for i, c in enumerate(cl):
				uc(i, c, t)
		if t < m:
			for i in range(n):
				ur(i)

		m -= t

	print(sum(cl))

main()

# !: TLE 8/15 https://usaco.org/current/viewsource.php?sid=6053798