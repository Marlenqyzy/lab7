a = int(input())
i = 0
test = False
while(2 ** i <= a):
    if((2**i) == a):
        test = True
        break
    i += 1
if test == True:
    print("YES")
else:
    print("NO")