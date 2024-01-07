n, k = map(int, input().split())
t = 0
o = [[0, 0, 0], [0, 1, 0], [1, 0, 0], [1, 1, 0]]

def check_delta(es, s, i): # 0 => L, 1 => R; 0 => +1, 1 => -1
	l = 0
	r = 0

	if es == 0:
		l = (-1)**s
	else:
		r = (-1)**s

	o[i][2] = abs(u + l - k*(s + r))
def make_delta(es, s, i): # 0 => L, 1 => R; 0 => +1, 1 => -1
	l = 0
	r = 0

	if es == 0:
		l = (-1)**s
	else:
		r = (-1)**s

	return [l, r]
 
for _ in range(n):
	u, s = map(int, input().split())

	while u != k*s:
		print("uny")
		for __ in range(4):
			check_delta(o[__][0], o[__][1], __)

		op = make_delta(*o[o.index(min(o, key=lambda x: x[2]))])
		u += op[0]
		s += op[1]
		t += 1

print(t)