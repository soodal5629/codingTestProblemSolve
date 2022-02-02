def dfs(idx, visit, graph,s):
    if visit[idx] == True: return False
    else:
        visit[idx] = True
        s.append(graph[idx])
        while s:
            now = s.pop()
            for i in now:
                if visit[i] == False:
                    visit[i] = True
                    s.append(graph[i])
        return True
def solution(n, computers):
    answer = 0
    graph = [[] for i in range(n)]
    for i in range(n):
        for j, value in enumerate(computers[i]):
            if value ==1: graph[i].append(j)
    visit = [False for _ in range(n)]
    s= []
    for i, value in enumerate(graph):
        flag = dfs(i, visit, graph,s)
        if flag == True: answer+=1
    return answer
