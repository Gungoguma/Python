init = []
for i in range(20):
    init.append([])
    for j in range(20):
        init[i].append(0)

for i in range(1, 20):
    a = [int(x) for x in input().split()]
    for j in range(1, 20):
        init[i][j] = a[j - 1]

num = int(input())
for i in range(num):
    x, y = map(int, input().split())
    for j in range(1, 20):
        if init[j][y] == 0:
            init[j][y] = 1
        else:
            init[j][y] = 0

        if init[x][j] == 0:
            init[x][j] = 1
        else:
            init[x][j] = 0

for i in range(1, 20):
    for j in range(1, 20):
        print(init[i][j], end=' ')
    print()
