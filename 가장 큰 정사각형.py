from collections import deque
def find(board, n,i, j, visit):
    res = 0
    x = i+1
    y = j+1
    cnt = 1
    while x<n and y<len(board[0]) and board[x][y]==1:
        flag = True
        for a in range(i, x+1):
            for b in range(j, y+1):
                if board[a][b] == 0:
                    flag = False
                    break
                else: visit[a][b] = True
            if flag == False: break
        if flag == False:
            break
        else:
            cnt+=1
            x+=1
            y+=1
    res = cnt**2
    return res
def solution(board):
    answer = 0
    n = len(board)
    visit = [[False for _ in range(len(board[0]))] for _ in range(n)]
    for i in range(n):
        for j in range(len(board[i])):
            if board[i][j] == 0: continue
            if visit[i][j]: continue
            answer = max(answer, find(board, n,i, j,visit))

    return answer
