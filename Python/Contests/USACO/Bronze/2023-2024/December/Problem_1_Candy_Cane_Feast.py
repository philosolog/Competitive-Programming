n, m = map(int, input().split())
cows = [int(x) for x in input().split()]
canes = [int(x) for x in input().split()]

for i in range(m):
	highest = 0
	newhighest = None

	for j in range(n):
		if cows[j] > highest:
			newhighest = cows[j]

			if canes[i] >= cows[j]:
				cows[j] += cows[j] - highest
			else:
				if canes[i] > highest:
					cows[j] += canes[i] - highest
				else:
					break
					
			highest = newhighest

for i in cows:
	print(i)