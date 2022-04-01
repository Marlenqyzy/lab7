a = int(input())
arr = input().split()
cnt = 0
check = False

for i in range(1, a):
    if (int(arr[i - 1]) >= 0 and int(arr[i]) >= 0) or (int(arr[i - 1]) < 0 and int(arr[i]) < 0):
        check = True
        break

if check == True:
    print("YES")
else:
    print("NO")
