s1 = str.lower(input())
s2 = str.lower(input())

index = [i for i in range(len(s1)) if s1[i] != s2[i]]

if len(index) != 0:
    index = index[0]
    
    print(int((ord(s1[index])-ord(s2[index]))/abs(ord(s1[index])-ord(s2[index]))))
else:
    print(0)
