def mnmm(a, b, c, d):
    if a <= b and a <= c and a <= d:
        print(a)
    elif b <= a and b <= c and b <= d:
        print(b)
    elif c <= a and c <= b and c <= d:
        print(c)
    else: 
        print(d)

a, b, c, d = input().split()

mnmm(int(a), int(b), int(c), int(d))