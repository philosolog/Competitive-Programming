for test in range(int(input())):
	aa = int(input())
	tl = []
	tllen = 0

	for array in range(aa):
		n = int(input())
		tllen += n
		sl = [int(x) for x in input().split()]
		tl += sl
		
	tl.sort(reverse=True)
	print(tl)
	print(sum(tl[:(aa-1)]) + tl[-1])