for t in range(int(input())):
	length = int(input())
	l = []

	for v in range(length):
		value = v + 1

		if value == 1:
			l.append(1)
		else:
			def checkmultiples(n):
				l.append(n)

				if n*2 <= length:
					checkmultiples(n*2)
				else:
					return False
			
			if value in l:
				pass
			else:
				checkmultiples(value)

	print(*l)