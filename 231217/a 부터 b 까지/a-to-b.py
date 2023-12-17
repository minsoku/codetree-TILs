a, b = map(int, input().split())
arr = [str(a)]
i = a
while i < b:
    if i % 2 == 1:
        i *= 2
        if i < b:
            arr.append(str(i))
    if  i % 2 == 0:
        i += 3
        if i < b:
            arr.append(str(i))

print(' '.join(arr))