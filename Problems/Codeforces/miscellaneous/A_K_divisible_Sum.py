# import math

# for _ in range(int(input())):
# 	n, k = map(int, input().split())
	
# 	print(math.ceil(k*math.ceil(n/k)/n))

# Note: Pigeonhole Principle; floor((n+k-1)/k) = ceil(n/k)
	
# In pure Python:
for _ in range(int(input())):
	n, k = map(int, input().split())
	
	print((k*((n+k-1)//k)+n-1)//n)