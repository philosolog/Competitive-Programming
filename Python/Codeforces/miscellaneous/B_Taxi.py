g = input()
n = [x for x in input().split()]
o = n.count("1")
tw = n.count("2")
th = n.count("3")
f = n.count("4")
o4 = o//4
o2 = (o%4)//2
tw1p = min(tw, o2)
tw2p = (tw-tw1p)//2
tw1 = (tw-tw1p)%2
o1 = o2-2*tw1p+(o%4)%2
th1 = max(o1, th)

print(o4 + tw2p + tw1 + th1 + f)