w = [ord(x)-97 for x in input()]
d = int(input())
s = int(input())
nw = [chr(x*d+s%26+97) for x in w]

print(*nw, sep="")