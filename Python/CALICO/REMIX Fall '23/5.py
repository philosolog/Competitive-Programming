for t in range(int(input())):
	h, w, d = [int(x) for x in input().split()]
	tb = h + d + 1

	def o(s, q1, q2):
		return [int(x) for x, c in enumerate(s) if c == q1 or c == q2]

	for ocn in range(h):
		l = input()
		s = [l[0]]

		for icn in range(tb):
			if icn != 0 and icn <= h-1:
				s = [*l[icn]]
				p = l[icn-1]
				pl = len(p)
				if d > 0:
					for i in o(p, "+", "\\"):
						if i+1 > len(s)-1:
							s += [" "]*(i-pl)+["\\"]
						else:
							s[i+1]=str("\\")
					d -= 1

		
		print("".join(s))