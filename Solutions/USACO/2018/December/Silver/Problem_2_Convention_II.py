def main():
	with open("convention2.in", "r") as fin:
		data = fin.readlines()
		
		for line in range(int(data[0])):
			a, t = map(int, data[line + 1].split())

			print(a, t)
	
	result = ""
	
	with open("convention2.out", "w") as fout:
		fout.write(result)

if __name__ == "__main__":
	main()