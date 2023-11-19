for t in range(int(input())):
	time = int(input())

	if time >= 180:
		print("canceled")
	elif time == 0:
		print("haha good one")
	else:
		print("berkeley"*(time//10)+"time")