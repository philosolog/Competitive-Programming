import sys
input = sys.stdin.buffer.readline

for _ in range(int(input())):
	A, B = map(int, input().split())

	if B == 1:
		print("NO")
	else:
		print("YES\n", A, A*B, A*(B+1))