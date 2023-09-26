for _ in range(int(input())):
    n, b, h = map(int, input().split())
    bases = list(map(int, input().split()))
    
    area = n * b * h / 2
    lastbase = bases[0]
    
    for base in bases[1:]:
        if base < (lastbase + h):
            area -= (b / (2 * h)) * (base - lastbase - h) ** 2
        lastbase = base
    
    print(area)