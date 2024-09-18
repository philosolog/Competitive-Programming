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

t = 0
n = 2

while n < 2000000:
	if isPrime(n):
		t += n

	n += 1
    
print(t)