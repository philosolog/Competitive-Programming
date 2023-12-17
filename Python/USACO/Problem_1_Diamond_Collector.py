n, k = map(int, input().split())
d = []

for i in range(n):
	d.append(int(input()))

nd = sorted(d)
m = 0

for i in range(len(nd)):
	for j in range(len(nd)-i):
		if nd[i+j] <= nd[i] + k:
			m = max(m, i+j)

print(m)