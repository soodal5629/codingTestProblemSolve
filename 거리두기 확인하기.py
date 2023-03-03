from collections import deque
def find_f(g):
    res = []
    for i in range(5):
        for j in range(5):
            if g[i][j] == 'P':
                res.append([i,j])
    return res

def bfs(g):
    p = find_f(g)
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    if len(p) == 0: return 1
    for i in p:
        d = deque()
        d.append((i, 0)) # ([x, y], cost)
        visit = [[False for _ in range(5)] for _ in range(5)]
        visit[i[0]][i[1]] = True
        while d:
            now, cost = d.popleft()
            x, y = now
            #visit[x][y] = True
            for j in range(4):
                a,b = x+dx[j], y+dy[j]
                if a<0 or a>4 or b<0 or b>4: continue
                if visit[a][b] == False and g[a][b] != 'X':
                    if g[a][b] == 'P' and cost+1 < 3: return 0
                    else:
                        visit[a][b] = True
                        d.append(([a,b], cost+1))
    return 1
def solution(places):
    answer = []
    for i in places:
        g = []
        for j in i:
            g.append(list(j))
        answer.append(bfs(g))
    return answer
