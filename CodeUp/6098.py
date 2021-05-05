init = []

for i in range(10):
    init.append(list(map(int, input().split())))
x, y = 1, 1

while True:
    if init[x][y] == 0:
        init[x][y] = 9
    elif init[x][y] == 2:
        init[x][y] = 9
        break

    if init[x][y+1] == 1 and init[x+1][y] == 1:
        break

    if init[x][y+1] != 1:
        y = y + 1
    elif init[x+1][y] != 1:
        x = x + 1


for i in range(10):
    for j in range(10):
        print(init[i][j], end=' ')
    print()
