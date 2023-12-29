import math

t = 8
n = (2*10**5)//t
s = " ".join([str(round(math.cos(x))+2) for x in range(n)])

print(str(t))

for _ in range(t):
	print(str(n))
	print(s)