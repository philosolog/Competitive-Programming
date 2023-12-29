import math

for _ in range(int(input())):
	n = int(input())
	a = sum([int(x) for x in input().split()])

	if math.sqrt(a).is_integer():
		print("YES")
	else:
		print("NO")