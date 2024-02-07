def o(st, sst): # TODO: Refactor
	c = s = 0
	
	while True:
		s = st.find(sst, s) + 1
		
		if s > 0:
			c += 1
		else:
			return c

for _ in range(10):
	s = input()
	c = 1
	sus = ["ookook", "ooga", "mookmook", "oogam", "oogum", "ugug"] # ooga and oogam what
	
	for sst in sus:
		c += o(s, sst)

# TODO: Implement JonathanZhu19's DP solution (https://cboj.ca/src/49649).