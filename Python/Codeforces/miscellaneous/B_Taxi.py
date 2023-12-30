g = int(input())
s = [int(_) for _ in input().split()]
tc = s.count(4)
c = [3]*s.count(3)
s = sorted([int(_) for _ in s if _ != 4 and _ != 3])

for i in range(len(s)-1, -1, -1): # Note: reversed(range(a, b)) -> range(b, a-1, -1) (range excludes the last value, and you have to identify the step)
	v = s[i]

	if v == 2:
		if 2 in c:
			c.remove(2)

			tc += 1
		else:
			c.append(2)
	elif v == 1:
		if 3 in c:
			c.remove(3)

			tc += 1
		elif 2 in c: # ?: Theoretically could put a for-loop here for scalability? Or should I find the first occurence of a "not 3" value?
			c[c.index(2)] += 1
		elif 1 in c:
			c[c.index(1)] += 1
		else:
			c.append(1)

print(tc + len(c))

# TODO: Optimize the solution to match the editorial.