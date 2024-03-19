for _ in range(int(input())):
	n, x = [int(x) for x in input().split()]
	o = 0
	a = "Yes"
	
	for v in input().split():
		o += int(v)%2
	
	if n == x or n == o:
		if o%2 == 0:
			a = "No"

	print(a)