from collections import deque
def bfs(n, m, g, x, y):
    d = deque()
    d.append((sx, sy))
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    cnt = 0
    v = [[1e9 for _ in range(m)] for _ in range(n)]
    v[x][y] = 1
    while d:
        x, y = d.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<m and g[nx][ny] != '*' and v[nx][ny] > (v[x][y]+1):
                d.append((nx, ny))
                v[nx][ny] = v[x][y] + 1
    return v[0][0]
                
n, m = map(int, input().split())
g = []
sx = sy= -1
for i in range(n):
    temp = list(input())
    if 'C' in temp:
        sx = i
        sy = temp.index('C')
    g.append(temp)
res = bfs(n, m, g, sx, sy)
print(res-1)
