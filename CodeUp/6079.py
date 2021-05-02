a = int(input())
b = 0
for i in range(1, a + 1):
    b = b + i
    if b >= a:
        print(i)
        break
