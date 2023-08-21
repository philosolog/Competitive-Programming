for test in range(int(input())):
	testers = int(input())
	tlist = [int(x) for x in input().split()]
	alist = list(map(lambda x: abs(x), tlist))
	c = 0
	n = 0

	for tester in range(testers):
		if tester < 0:
			n += 1
	
	if n%2 != 0:
		for tester in range(testers):
			if tester == -min(alist): # if this goes below 0?
				c += tlist[tester]
			else:
				if tester == 0:
						c += tlist[tester]
				else:
					if c+tlist[tester] >= c*alist[tester]:
						c += tlist[tester]
					else:
						c *= tlist[tester]
	else:
		for tester in range(testers):
			if tester == 0:
				c += tlist[tester]
			else:
				if c+tlist[tester] >= c*tlist[tester]:
					c += tlist[tester]
				else:
					c *= tlist[tester]
	
	print(c)