total = 0
f = [0, 1]
current = 0
n = 2

while current <= 4000000:
	f.append(f[n-1] + f[n-2])
	
	if (f[n-1] + f[n-2]) % 2 == 0:
		total += f[n-1] + f[n-2]
	
	current = f[n-1] + f[n-2]
	n += 1

print(total)