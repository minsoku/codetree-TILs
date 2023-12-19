a = input()
arr = a.split()
n = int(arr[0])
m = int(arr[1])
temp = n

n = m
m = temp

print("%d %d" %(n, m))