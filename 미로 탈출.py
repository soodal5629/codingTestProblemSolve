from collections import deque
def bfs(g, start, end, l):
    q = deque()
    opened = False
    q.append((start, 1))
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    visit = [[False for _ in range(len(g[0]))] for _ in range(len(g))]
    g[start[0]][start[1]] = 1
    visit[start[0]][start[1]] = True
    while q:
        now, cost = q.popleft()
        x, y =now
        for i in range(4):
            if x+dx[i] < 0 or y+dy[i] < 0 or y+dy[i] >= len(g[0]) or x+dx[i] >= len(g): continue
            if opened == False and x+dx[i] == l[0] and y+dy[i] == l[1]:
                opened = True
                q.clear()
                visit = [[False for _ in range(len(g[0]))] for _ in range(len(g))]
                g[x+dx[i]][y+dy[i]] = cost+1
                visit[x+dx[i]][y+dy[i]] = True
                q.append(([x+dx[i], y+dy[i]], cost+1))
                break
            if opened == True and x+dx[i] == end[0] and y+dy[i] == end[1]:
                return cost
            if g[x+dx[i]][y+dy[i]] != 'X' and visit[x+dx[i]][y+dy[i]] == False:
                g[x+dx[i]][y+dy[i]] = cost+1
                visit[x+dx[i]][y+dy[i]] = True
                q.append(([x+dx[i], y+dy[i]], cost+1))
    x,y =end
    if g[x][y] == 0 or visit[l[0]][l[1]] == False: return -1
    else: return g[x][y]-1

def solution(maps):
    answer = 0
    g = []
    for i in maps:
        g.append(list(i))
    start = []
    end = []
    l = []
    for i in range(len(g)):
        for j in range(len(g[0])):
            if g[i][j] == 'S': 
                start = [i,j]
                g[i][j] = 0
            elif g[i][j] == 'E':
                end = [i,j]
                g[i][j] = 0
            elif g[i][j] == 'L': 
                l = [i,j]
                g[i][j] = 0
            elif g[i][j] == 'X': continue
            elif g[i][j] == 'O': g[i][j] = 0
    answer = bfs(g, start, end, l)
    return answer
