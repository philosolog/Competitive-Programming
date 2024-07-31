import math

for _ in range(int(input())):
	n = int(input())

	print(math.floor(math.sqrt(n)) + math.floor(math.cbrt(n)) - math.floor(math.cbrt(math.sqrt(n))))

# !: This problem fails to be read by the CF judge due to "import math" being unsupported ? (it was forced for my PIE solution). The canonical solution is to search the solution space. Check my Java solution (../B_Squares_and_Cubes.java).