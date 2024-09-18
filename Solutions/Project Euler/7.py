def isPrime(k):
	if (k <= 1):
		return 0
	if (k == 2 or k == 3):
		return 1
	if (k % 2 == 0 or k % 3 == 0):
		return 0
	
	for i in range(5, 1 + int(k ** 0.5), 6):
		if (k % i == 0 or k % (i + 2) == 0):
			return 0

	return 1
def nThPrime(n):
	i = 2
	
	while(n > 0):
		if(isPrime(i)):
			n -= 1

		i += 1

	i -= 1
	
	return i

print(nThPrime(10001)) # 104743

# TODO: Check why my old solution failed