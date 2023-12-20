x, y, m = map(int, input().split())
max = 0

for l in range(m//x):
	r = m//x - l

	if l*x + r*y <= m and l*x + r*y > max:
		max = l*x + r*y

print(max)