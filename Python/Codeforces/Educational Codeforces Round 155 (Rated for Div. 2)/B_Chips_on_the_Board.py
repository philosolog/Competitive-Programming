for t in range(int(input())):
	n = int(input())
	a = [int(x) for x in input().split()]
	b = [int(x) for x in input().split()]

	print(min(min(a)*n + sum(b), min(b)*n + sum(a)))