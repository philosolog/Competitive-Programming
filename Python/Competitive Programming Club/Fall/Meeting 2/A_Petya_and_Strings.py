s1 = str.lower(input())
s2 = str.lower(input())

index = next((i for i in range(min(len(s1), len(s2))) if s1[i]!=s2[i]), None)

if index is not None:
	print(int((ord(s1[index])-ord(s2[index]))/abs(ord(s1[index])-ord(s2[index]))))
else:
    print(0)