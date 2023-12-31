for _ in range(int(input())):
	n, k = map(int, input().split())
	m = [int(_)%k or k for _ in input().split()]
	
	print(*[x+1 for x in sorted(range(n), key=m.__getitem__, reverse=True)]) # ?: How does this work syntactically? (sorted(m, reverse=True)) vs. (sorted(range(n), key=m.__getitem__, reverse=True))?