num = int(input())
a = list(map(int, input().split()))

for i in range(num):
    a[i] = int(a[i])

b = []
for i in range(24):
    b.append(0)

for i in range(num):
    b[a[i]] += 1

for i in range(1, 24):
    print(b[i], end=' ')
