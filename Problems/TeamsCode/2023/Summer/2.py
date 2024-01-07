#reference for now: for test in range(int(input())):
#testcases = int(input())
for test in range(int(input())):
    output = 0
    n = int(input())
    nelements = [int(z) for z in input().split()]   #somethings wrong here...
    ideal = sorted(nelements)
    if nelements == ideal:
        print(output)
    else:
        for a in range(n):
            if ideal[a] != nelements[a]:
                output += 1
        print(output)    


#a different version? 
for test in range(int(input())):
    output = 0
    n = int(input())
    ugh = input()
    nelements =[]
    for i in ugh:
        nelements.append(int(i))
    ideal = sorted(nelements)
    if nelements == ideal:
        print(output)
    else:
        for a in range(n):
            if ideal[a] != nelements[a]:
                output += 1
        print(output)    


#old code before i knew how the input works T_T
'''x= input()
lx = [int(i) for i in x]
testcases = lx[0]
lx.remove(testcases)
while len(lx) > 1:
  n = lx[0]
  lx.remove(n)
  inwork = []
  y = 0
  output = 0
  while y != n:
    inwork.append(lx[0])
    lx.remove(lx[0])
    y+=1
  whatwewant = sorted(inwork)
  if whatwewant == inwork:
    print (output)
  else:
    for a in range(n):
      if inwork[a] != whatwewant[a]:
        output += 1
    print(output)'''
    