import heapq
def solution(maps):
    answer = 0
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    n = len(maps)
    m = len(maps[0])

    q = []
    x = 0
    y = 0
    cost = 1
    heapq.heappush(q, (cost, x, y))
    while q:
        cost, x, y =heapq.heappop(q)
        maps[x][y] = cost+1
        if x==n-1 and y == m-1: break
        for i in range(4):
            if x+dx[i]<0 or x+dx[i]>=n or y+dy[i]<0 or y+dy[i]>=m: continue 
            if maps[x+dx[i]][y+dy[i]] == 1: 
                maps[x+dx[i]][y+dy[i]] == cost+1
                heapq.heappush(q, (cost+1,x+dx[i],y+dy[i]))
    if maps[n-1][m-1] == 1 : answer = -1
    else: answer = maps[n-1][m-1]-1
    return answer
