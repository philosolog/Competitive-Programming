for _ in range(int(input())):
	n = int(input())
	l = list(map(int, input().split()))[1:n-1]
	rl = sum([x%2 for x in l])
	a = 0


	for v in l:
		if v%2 == 0:
			rl -= 1
		
		a += (v + v%2)//2

	if rl <= 0:
		print(a)
	else:
		print(-1)