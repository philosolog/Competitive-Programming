import math

def pfactors(n):
	plist = []

	while n % 2 == 0:
		plist.append(2),
		n = n / 2
	for i in range(3, int(math.sqrt(n))+1, 2):
		while n%i == 0:
			plist.append(i)
			n = n / i

	if n > 2:
		plist.append(n)

	return plist

for t in range(int(input())):
	x = int(input())

	print(len(pfactors(x)) + 1)