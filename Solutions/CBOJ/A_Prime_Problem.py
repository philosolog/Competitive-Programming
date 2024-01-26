l = []

for _ in range(int(input())):
	a, b = map(int, input().split())

	if len(l) >= b:
		print(l[max(0, a-2):max(0, b-2)].count(True))
	else:
		l.extend([True]*(b-len(l))) # 0 -> 2

		 