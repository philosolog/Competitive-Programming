for _ in range(int(input())):
    a, b, n = map(int, input().split())
    ts = map(int, input().split())
    tt = b

    for t in ts:
        if t > a:
            t = a - 1
        tt += t

    print(tt)