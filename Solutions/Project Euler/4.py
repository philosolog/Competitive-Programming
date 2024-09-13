answer = 0

for l in range(999, 99, -1):
	for r in range(999, 99, -1):
		if str(l*r) == str(l*r)[::-1]:
			answer = max(answer, l*r)
			
			break

print(answer)