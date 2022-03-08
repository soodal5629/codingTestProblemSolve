from collections import deque
def solution(board, moves):
    answer = 0
    d = deque()
    n = len(board)
    for i in moves:
        index = i - 1
        for x in range(n):
            if board[x][index] == 0: continue
            else:
                if len(d)>0 and d[-1] == board[x][index]:
                    answer += 2
                    d.pop()
                else: d.append(board[x][index])
            board[x][index] = 0
            break
    return answer
