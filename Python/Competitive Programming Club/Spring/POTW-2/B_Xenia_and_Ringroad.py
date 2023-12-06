n, m = [int(x) for x in input().split()]
t = [int(x) for x in input().split()]
s = [v for i, v in enumerate(t) if i == 0 or v != t[i-1]]
d = []

for i, h in enumerate(s):
	if i == 0:
		d.append((h-1)%n)
	else:
		d.append((h-s[i-1])%n)

print(sum(d))