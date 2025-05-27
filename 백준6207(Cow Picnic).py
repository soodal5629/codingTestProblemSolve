from collections import deque
def find(now, g, temp, n):
    d = deque()
    d.append(now)
    v = [False] * (n+1)
    while d:
        now = d.popleft()
        temp[now]+=1
        v[now] = True
        for i in g[now]:
            if not v[i]:
                d.append(i)
                v[i] = True 
k, n, m = map(int, input().split())
p = []
for _ in range(k):
    p.append(int(input()))

g = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)

temp = [0] * (n+1)
for i in p:
    find(i, g, temp, n)
print(temp[1:].count(k))
