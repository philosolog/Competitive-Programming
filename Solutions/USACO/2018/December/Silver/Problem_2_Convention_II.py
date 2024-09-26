def main():
	from bisect import bisect_left

	with open("convention2.in", "r") as fin:
		data = fin.readlines()
		queue = []

		for line in range(int(data[0])):
			queue.append(list(map(int, data[line + 1].split())))

		queue.sort(key=lambda x: x[0])

		time = 0
		longest = 0

		while len(queue) > 0:
			query = queue[0]

			if time <= query[0]:
				time = query[0] + query[1]
				queue.pop(0)
			else:
				for i in range(bisect_left(queue, [time, 0])-1, -1, -1):
					longest = max(longest, time - queue[i][0])
					time += queue[i][1]
					queue.pop(i)

			
	
	result = str(longest)
	
	with open("convention2.out", "w") as fout:
		fout.write(result)

if __name__ == "__main__":
	main()