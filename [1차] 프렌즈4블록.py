from collections import deque
def find(g,i,j, visit):
    
    s = deque()
    s.append([i,j])
    res = set()
    res.add((i,j))
    while s:
        x, y = s.popleft()
        visit[x][y] = True
        if x<len(g)-1 and y<len(g[0])-1:
            if g[x][y]!='' and g[x][y] == g[x][y+1] and g[x][y] ==g[x+1][y] and g[x][y] ==g[x+1][y+1]:
                if visit[x][y+1] == False: 
                    s.append([x, y+1])
                    res.add((x, y+1))
                if visit[x+1][y] == False: 
                    s.append([x+1, y])
                    res.add((x+1, y))
                if visit[x+1][y+1] == False: 
                    s.append([x+1,y+1])
                    res.add((x+1, y+1))
    return res

def burst(s, g):
    for i in s:
        x, y = i
        g[x][y] = ''
    return g

def move(g):
    m = len(g)
    n = len(g[0])
    i = j = 0
    while i<m-1:
        if g[i][j] != '' and g[i+1][j] == '':
            g[i+1][j] = g[i][j]
            g[i][j] = ''
            i=0
            j=0
            continue
        if j<n-1:
            j+=1
        else:
            i+=1
            j=0
    return g
def solution(m, n, board):
    answer = 0
    g=[[] for _ in range(m)]
    cnt = 0 
    visit = [[False for a in range(n)] for b in range(m)]
    for i in board:
        for j in i:
            g[cnt].append(j)
        cnt+=1
    i = 0
    j = 0

    flag = True
    while flag:
        s = set()
        visit = [[False for a in range(n)] for b in range(m)]
        for i in range(m):
            for j in range(n):
                temp = find(g, i, j, visit)
                if len(temp)>1: 
                    s.update(temp)
                    flag = True
        if len(s) <= 1 :
            break
        else:
            answer += len(s)
            g=burst(s, g)
            g=move(g)
        s.clear()  
    return answer

