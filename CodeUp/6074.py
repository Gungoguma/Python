a = ord(input())
b = ord("a")
while True:
    print(chr(b), end=' ')
    b = b + 1
    if a < b:
        break
