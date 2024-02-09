import sys

sys.setrecursionlimit(100000)

n, m = map(int, input().split())
p = []

for _ in range(n):
	p.append(list(map(int, input().split())))

x, y, c, t = map(int, input().split())
ic = [[False for r in range(m)] for c in range(n)]
tt = [[x-1, y-1]]

def check(i, j, ov):
	if 0 <= i < n and 0 <= j < m:
		if abs(p[i][j]-ov) <= t and ic[i][j] == False:
			return True
	
	return False

while tt:
	i, j = tt.pop(0)
	ov = p[i][j]

	if check(i+1, j, ov):
		ic[i+1][j] = True

		tt.append([i+1, j])

		p[i+1][j] = c
	if check(i-1, j, ov):
		ic[i-1][j] = True
		
		tt.append([i-1, j])

		p[i-1][j] = c
	if check(i, j+1, ov):
		ic[i][j+1] = True
		
		tt.append([i, j+1])

		p[i][j+1] = c
	if check(i, j-1, ov):
		ic[i][j-1] = True
		
		tt.append([i, j-1])

		p[i][j-1] = c

for l in p:
	print(*l)