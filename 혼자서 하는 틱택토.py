def check(g, c):
    if g[0][0] == c and g[1][1] == c and g[2][2] == c : return True
    if g[0][2] == c and g[1][1] == c and g[2][0] == c : return True
    for i in range(3):
        if g[i][0] == c and g[i][1] == c and g[i][2] == c: return True
    for i in range(3):
        flag = True
        for j in range(3):
            if g[j][i] != c: 
                flag = False
                break
        if flag: return True
    return False
    
def find(g):
    o = x = 0
    for i in range(3):
        for j in range(3):
            if g[i][j]== 'O': o+=1
            elif g[i][j]== 'X': x+=1
    if x > o: return 0
    if o == 0 and x ==0 : return 1
    if o - x > 1: return 0
    if check(g, 'O'):
        if check(g, 'X') == False and o-x ==1: return 1
        else: return 0
    if check(g, 'X'):
        if check(g, 'O') == False and o == x : return 1
        else: return 0
    else:
        if o-x<=1: return 1
        else: return 0
    return 1    
def solution(board):
    answer = -1
    g = []
    for i in board:
        g.append(list(i))
    answer = find(g)
    return answer
