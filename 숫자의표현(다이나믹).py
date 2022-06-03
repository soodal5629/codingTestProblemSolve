def solution(n):
    answer = 1
    index = (n//2)+2
    d = [[0 for _ in range(index+1)] for _ in range(index+1)]
    for i in range(1, index):
        if i ==1 :
            d[1][i] = 1
        else:
            d[1][i] = i + d[1][i-1]

    cnt = 1
    for i in range(2, index):
        for j in range(i, index):
            d[i][j] = d[i-1][j] - cnt
            
        cnt+=1
    for i in range(1, index):
        answer += d[i].count(n)
    if n == 1 or n==2: answer = 1   
    return answer
