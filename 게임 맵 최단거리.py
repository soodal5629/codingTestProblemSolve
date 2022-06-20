from collections import deque

def bfs(maps):
    d = deque()
    d.append([0, 0, 1])
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    while d:
        x, y, cost = d.popleft()
        for i in range(4):
            if x+dx[i]<0 or x+dx[i]>=len(maps) or y+dy[i]<0 or y+dy[i]>=len(maps[0]): continue
            if maps[x+dx[i]][y+dy[i]] == 1:
                maps[x+dx[i]][y+dy[i]] = cost+1
                d.append([x+dx[i], y+dy[i], cost+1])
    return maps[len(maps)-1][len(maps[0])-1]
def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    if maps[n-1][m-2] == 0 and maps[n-2][m-1] == 0:
        answer = -1
    else:
        answer = bfs(maps)
        if answer ==1: answer = -1
    return answer
