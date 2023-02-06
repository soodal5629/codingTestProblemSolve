from collections import deque
def bfs(g, x, y):
    dx=[-1,1,0,0]
    dy =[0,0,-1,1]
    d = deque()
    d.append((x, y))
    res = 0
    while d:
        x, y = d.popleft()
        if g[x][y] == 'X': continue
        res+=int(g[x][y])
        g[x][y] = 'X'
        for i in range(4):
            if x+dx[i] < 0 or x+dx[i] >= len(g) or y+dy[i] < 0 or y+dy[i] >= len(g[0]): continue
            if g[x+dx[i]][y+dy[i]] != 'X':
                d.append((x+dx[i], y+dy[i]))
    return res
def solution(maps):
    answer = []
    g = []
    for i in maps:
        g.append(list(i)) 
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if g[i][j] == 'X': continue
            temp = bfs(g, i, j)
            answer.append(temp)
    if len(answer) == 0: answer = [-1]
    answer.sort()
    return answer
