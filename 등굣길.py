def solution(m, n, puddles):
    answer = 0
    road = [[0 for i in range(m)] for j in range(n)]
    for i in puddles:
        x,y= i[0]-1, i[1]-1
        road[y][x] = 1e9

    for i in range(n):
        for j in range(m):
            if i == 0 and j==0: 
                road[i][j] =1
                continue
            if road[i][j] == 1e9: continue
            else: #순서가 매우 중요함..
                if road[i-1][j] == 1e9 and road[i][j-1] == 1e9:
                    road[i][j] = 1e9
                elif road[i-1][j] == 1e9:
                    road[i][j] = road[i][j-1]
                elif road[i][j-1] == 1e9:
                    road[i][j] = road[i-1][j]
                elif i==0:
                    road[i][j] =road[i][j-1]
                elif j==0:
                    road[i][j] = road[i-1][j]
                else:
                    if i>=1 and j>=1:road[i][j] =(road[i-1][j]+road[i][j-1])%1000000007                
    if answer != 1e9: answer = road[n-1][m-1]
    else: answer = 0
    return answer
