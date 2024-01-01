for t in range(int(input())):
	bricks = int(input())
	height = bricks//3

	print((2^(height+1)-2)%3359232)