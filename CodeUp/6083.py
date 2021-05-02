a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
num = 0

for i in range(c):
    for j in range(b):
        for k in range(a):
            print("{} {} {}" .format(i, j, k))
            num += 1
print(num)
