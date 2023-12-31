import math

for _ in range(int(input())):
	n, k = map(int, input().split())
	
	print(math.ceil(k*math.ceil(n/k)/n))

# Note: Pigeonhole Principle