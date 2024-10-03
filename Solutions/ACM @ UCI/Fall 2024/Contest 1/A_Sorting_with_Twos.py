import math

for _ in range(int(input())):
	n = int(input())
	l = [int(x) for x in input().split()]
	p = [2**x for x in range(int(math.log2(n)))]
	answer = "YES"
	
	for i in range(len(p)-1):
		# print(p[i], p[i+1])
		for j in range(p[i], p[i+1]):
			print(j, j+1)
			if l[j-1] > l[j]:
				answer = "NO"
				break
		# print("bee")

	print(answer)