count = 1
primes = [2]
current = 3

while count <= 10001:
	is_prime = True

	for prime in primes:
		if current % prime == 0:
			is_prime = False

			break

	if is_prime:
		count += 1
		primes.append(current)

	current += 1

print(current)