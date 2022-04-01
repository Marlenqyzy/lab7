v = int(input())
t = int(input())

s = v * t

if s > 0:
    if s > 109:
        while s > 109:
            s = s - 109
    print(s)
else:
    if s < -109:
        while(s < -109):
            s = s + 109
    print(s + 109)