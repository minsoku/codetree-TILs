n = int(input())
arr = []
for i in range(n, 101):
    if i < 60:
        arr.append("F")
    elif i < 70:
        arr.append("D")
    elif i < 80:
        arr.append("C")
    elif i < 90:
        arr.append("B")
    else:
        arr.append("A")

print(' '.join(arr))