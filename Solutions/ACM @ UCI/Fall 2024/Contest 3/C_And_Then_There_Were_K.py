for _ in range(int(input())):
	n = int(input())
	
	while n&(n-1) != 0:
		n &= n-1

	print(n-1)