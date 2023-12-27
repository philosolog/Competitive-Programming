# 
for _ in range(int(input())):
	n = int(input())
	current_integer = 1
	diagonal_offset = 0
	m = [[0]*n for __ in range(n)]

	if n == 1:
		print(1)
	elif n == 2:
		print(-1)
	else:
		for i in range(2*n-1):
			if diagonal_offset == 0:
				for j in range(n):
					m[j][j] = current_integer
					current_integer += 1
				
				diagonal_offset += 1
			else:
				for j in range(n-diagonal_offset):
						m[j][j+diagonal_offset] = current_integer
						current_integer += 1
				for j in range(n-diagonal_offset):
						m[j+diagonal_offset][j] = current_integer
						current_integer += 1
				
				diagonal_offset += 1
		for i in m:
			print(*i)