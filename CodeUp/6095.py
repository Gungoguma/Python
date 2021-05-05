init = []
for i in range(20):
    init.append([])
    for j in range(20):
        init[i].append(0)

num = int(input())
for i in range(num):
    x, y = input().split()
    init[int(x)][int(y)] = 1

for i in range(1, 20):
    for j in range(1, 20):
        print(init[i][j], end=' ')
    print()
