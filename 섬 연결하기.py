def find(n, parent):
    while parent[n] != n:
        n = parent[n]
        find(n,parent)
    return parent[n]

def union(a,b,parent):
    a = find(a, parent)
    b = find(b, parent)
    if a<b:
        parent[b]=a
    else:
        parent[a] = b
def solution(n, costs):
    answer = 0
    graph = []
    parent = [0 for _ in range(n)]
    for i in range(n):
        parent[i] = i 
    for i in costs:
        a,b,c = i
        graph.append((c,a,b))
    graph.sort()
    
    for i in graph:
        cost, a, b = i
        if find(a, parent) != find(b, parent):
            union(a,b,parent)
            answer += cost
    return answer
