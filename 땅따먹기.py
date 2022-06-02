def solution(land):
    answer = 0
    m = len(land)
    n = len(land[0])
    arr=[]
    d = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            d[i][j] = land[i][j]

    index = 0
    for i in range(1, m):
        if i==1: j = index
        for j in range(n):
            temp = d[i][j]
            for k in range(n):
                if k == j: continue
                if d[i][j] < temp+d[i-1][k]:
                    d[i][j] = temp+d[i-1][k]
                    index = k
    answer = max(d[m-1])
    return answer
