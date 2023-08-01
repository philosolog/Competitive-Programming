n = int(input())
nb = bin(n)[2:]

try:
	nblo = nb.rfind("1")
	nblz = nb.rfind("0", 0, nblo)
	nbn = [*nb]
	nbn[nblo] = "0"
	nbn[nblz] = "1"
	
	print(int("".join(nbn), 2))
except:
	print(-1)