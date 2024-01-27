l = []

for _ in range(int(input())):
	a, b = map(int, input().split())
	c = len(l) - 1

	if b - 1 > c:
		al = [True for __ in range(b-1-c)]

		for i, v in enumerate(l):
			if v == True:
				if i != 0:

				else:
					l[i] = False


	print(l[a-1:b-1].count(True))