from collections import deque
def find(g, x, y):
    v = [[0 for _ in range(len(g[0]))] for _ in range(len(g))]
    d = deque()
    d.append([x, y])
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    v[x][y] = 1
    while d:
        x, y = d.popleft()
        if g[x][y] == 'G':
            return v[x][y]-1
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            while True:
                if nx < 0 or nx >= len(g) or ny < 0 or ny >= len(g[0]):
                    nx -= dx[i]
                    ny -= dy[i]
                    break
                elif g[nx][ny] == 'D':
                    nx -= dx[i]
                    ny -= dy[i]
                    break
                else:
                    nx += dx[i]
                    ny += dy[i]
            if v[nx][ny] == 0:
                v[nx][ny] = v[x][y]+1
                d.append([nx, ny])  
    return -1

def solution(board):
    answer = 0
    g = []
    for i in board:
        g.append(list(i))
    x = y = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if g[i][j] == 'R':
                x = i
                y = j
                break
    answer = find(g, x, y)
    return answer
