t = 8
n = (2*10**5)//t
x = -10**9
y = 10**9

print(str(t))
for _ in range(t):
	print(n)
	
	for _ in range(n):
		print(str(x+_) + " " + str(y-_))