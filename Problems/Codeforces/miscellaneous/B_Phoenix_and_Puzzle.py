import math

def check_square(n): # ?: Which square check has the best time complexity?
	return (math.sqrt(n)).is_integer()

for _ in range(int(input())):
	n = int(input())
	
	if n%2 == 0 and check_square(n/2):
		print("YES")
	elif n%4 == 0 and check_square(n/4):
		print("YES")
	else:
		print("NO")