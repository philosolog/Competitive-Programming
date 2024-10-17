for _ in range(int(input())):
	n = input()
	s = set()
	l = None
	answer = "YES"

	for v in input():
		if v in s and l != v:
				answer = "NO"

				break
		else:
			l = v
			s.add(v)

	print(answer)
