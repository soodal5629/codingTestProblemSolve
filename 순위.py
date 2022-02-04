def solution(n, results):
    answer = 0
    graph = [[0 for i in range(n+1)] for j in range(n+1)]
    for i in results:
        a, b = i
        graph[a][b] = 1
        graph[b][a] = -1
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if graph[i][k] == 1 and graph[k][j] == 1:
                    graph[i][j] = 1
                if graph[i][k] ==-1 and graph[k][j] == -1:
                    graph[i][j] = -1

    for i in range(1,n+1):
        if graph[i].count(0)==2:
            answer +=1
    return answer
