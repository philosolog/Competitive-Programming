l = []

for _ in range(int(input())):
	a, b = map(int, input().split())

	if len(l) < b:
		s = len(l)

		l.extend([True]*(b-s-1)) # 0 -> 2
		
		for i, v in enumerate(l):
			tv = i+2

			if v == True:
				if tv*2 <= b:
					fb = s//tv + 2 # !: I am dying here. :) The algo. improperly counts past the first extend after 1000?
					lb = (fb+b-s-1)//tv

					print(fb)
					for j in range(fb, lb+1):
						if j*tv <= b:
							if l[j*tv-2] != False: # ?: Necessary?
								l[j*tv-2] = False
						else:
							break
				else:
					break
	print("-------------------")
	# print(l[max(0, a-2):b-1].count(True)) # ?: max(0, b-2).. b-1?