init = []
a, b = map(int, input().split())
num = int(input())

for i in range(a):
    init.append([])
    for j in range(b):
        init[i].append(0)

for i in range(num):
    l, d, x, y = map(int, input().split())
    for j in range(l):
        if d == 0:
            init[x-1][y-1+j] = 1
        else:
            init[x-1+j][y-1] = 1

for i in range(a):
    for j in range(b):
        print(init[i][j], end=' ')
    print()
