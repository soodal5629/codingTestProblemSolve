n = int(input())
arr = list(map(int, input().split()))
arr.sort()

f = arr[0+n]
s = arr[n - 1 + n]
print(s-f)
