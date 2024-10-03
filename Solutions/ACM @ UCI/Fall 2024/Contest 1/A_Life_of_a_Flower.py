for _ in range(int(input())):
	n = int(input())
	d = [int(x) for x in input().split()]
	h = 1
	l = -1
	answer = None

	for v in d:
		if v == l:
			if v == 0:
				answer = -1

				break
			elif v == 1:
				h += 5
		else:
			if v == 0:
				l = 0
			else:
				h += 1
				l = 1
	
	print(answer if answer else h)