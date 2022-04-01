a = input()

cnt = ''
for i in range(0, len(a)):
    cnt += a[len(a) - i - 1]

print(int(cnt))