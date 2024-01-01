import math

for t in range(int(input())):
	def min_swaps_to_alternate(binary_string):
		swapCount = 0
		prevChar = binary_string[0]
		
		for char in binary_string[1:]:
			if char == prevChar:
				swapCount += 1
				prevChar = '0' if char == '1' else '1'
			else:
				prevChar = char

		return swapCount
	
	l = input()
	sequence = min_swaps_to_alternate(l)
	print(sequence, (2**sequence + 2*(sequence-1))%998244353)