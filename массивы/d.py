a = int(input())
arr = input().split()
cnt = 0

for i in range(1, a):
    if int(arr[i - 1]) < int(arr[i]):
        cnt += 1
print(cnt)