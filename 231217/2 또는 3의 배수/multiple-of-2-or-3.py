n = int(input())
arr = []
for i in range(1, n+1):
    if i % 2 == 0 or i % 3 == 0:
        arr.append("1")
    else:
        arr.append("0")


print(' '.join(arr))