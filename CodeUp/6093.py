num = int(input())
a = list(map(int, input().split()))

for i in range(num):
    a[i] = int(a[i])

for i in range(num-1, -1, -1):
    print(a[i], end=' ')
