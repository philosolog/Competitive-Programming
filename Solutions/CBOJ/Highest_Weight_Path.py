n = int(input())
l = []

for _ in range(n):
	l.append(list(map(int, input().split())))
for i in range(n):
	for j in range(i+1):
		p = l[i-1]
		p_1 = p[j-1] if j != 0 else 0
		p_2 = p[j] if i >= j+1 else 0

		l[i][j] += max(p_1, p_2)

print(max(l[-1]))