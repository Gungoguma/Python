a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

print((b if a > b else a) if (b if a > b else a) < c else c)
