w = [ord(x)-97 for x in input("Give a string to encode: ")] # TODO: Check for non-alphabetic characters. Alter support for different capitalization?
d = None
s = None

while True:
	d = input("Give a divisor: ")

	try:
		d = int(d)

		break
	except ValueError:
		print("Denote a valid integer.")
while True:
	s = input("Give a shift: ")

	try:
		s = int(s)

		break
	except ValueError:
		print("Denote a valid integer.")
		
nw = "".join([chr(x*d+s%26+97) for x in w])
a = ""
b = ""
c = ""

if d > 1 or d < 0:
	a = str(d) + "x + "
elif d == 1:
	a = "x + "
elif d == 0:
	a = ""
if s != 1:
	b = str(s) + "mod(26)"
else:
	b = "mod(26)"
if a + b == "":
	c = 0
else:
	c = a + b
	
print('The string "' + nw + '" is the encoded output of the following affine cipher: p(x) = ' + c)