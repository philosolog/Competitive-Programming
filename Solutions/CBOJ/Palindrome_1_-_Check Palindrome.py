s = input()
t = "YES"

for i in range(len(s)//2):
    if s[i] != s[-(i+1)]:
        t = "NO"
        
print(t)