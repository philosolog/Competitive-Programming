for _ in range(int(input())):
	n = int(input())
	s = input()
	
	print("YES" if s[0] != s[-1] else "NO") # Note: s[-1] is the same as s[len(s)-1], I think.