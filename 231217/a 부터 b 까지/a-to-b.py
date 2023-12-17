a, b = map(int, input().split())
arr = [str(a)]
i = a
while i < b:
    if i < b and i % 2 == 1:
        i *= 2
        arr.append(str(i))
    if i < b and i % 2 == 0:
        i += 3
        arr.append(str(i))

print(' '.join(arr))