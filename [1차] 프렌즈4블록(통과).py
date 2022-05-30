from collections import deque
def find(g,i,j):
    res = set()
    res.add((i,j))
    x, y = i, j
    if x<len(g)-1 and y<len(g[0])-1:
            if g[x][y]!='' and g[x][y] == g[x][y+1] and g[x][y] ==g[x+1][y] and g[x][y] ==g[x+1][y+1]:
                res.add((x, y+1))
                res.add((x+1, y))
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
    for i in range(n):
        temp = deque()
        for j in range(m):
            if g[j][i] != '': temp.append(g[j][i])
        for j in range(m - len(temp)):
            temp.appendleft('')
        for j in range(m):
            g[j][i] = temp[j]
    return g

def solution(m, n, board):
    answer = 0
    g=[[] for _ in range(m)]
    cnt = 0 
    for i in board:
        for j in i:
            g[cnt].append(j)
        cnt+=1
    i = 0
    j = 0

    flag = True
    while True:
        s = set()
        for i in range(m):
            for j in range(n):
                temp = find(g, i, j)
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
