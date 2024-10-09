for _ in range(int(input())):
	W, H = map(int, input().split())
	x1, y1, x2, y2 = map(int, input().split())
	w, h = map(int, input().split())

	if h + (y2-y1) <= H or w + (x2-x1) <= W:
		a = []
		
		if h + (y2-y1) <= H:
			a.append(h-y1)
		if w + (x2-x1) <= W:
			a.append(w-x1)

		print(min(a))
	else:
		print(-1)