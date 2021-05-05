num = int(input())
a = list(map(int, input().split()))

for i in range(num):
    a[i] = int(a[i])

small = a[0]
for i in range(num):
    if small > a[i]:
        small = a[i]

print(small)
