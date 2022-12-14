from collections import defaultdict
def solution(e, starts):
    answer = []
    d = [[0 for i in range(e+1)] for j in range(1+e)]
    m = min(starts)
    dict = defaultdict(int)
    for i in range(1, e+1):
        for j in range(1, e+1):
            temp = i*j
            if  temp > e: break
            d[i][j] = temp
            dict[temp] +=1
    
    for i in starts:
        temp = [0,0]
        for j in range(i, e+1):
            if temp[1] < dict[j]: temp = [j, dict[j]]
        answer.append(temp[0])
    return answer
