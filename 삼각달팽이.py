def solution(n):
    answer = []
    x = -1
    y = 0
    cnt = 0
    num = 1
    arr = [[0 for i in range(n)] for j in range(n)]
    while cnt<n:
        for i in range(cnt, n):            
            if cnt%3 == 0:
               x+=1
            elif cnt%3 == 1:
                y+=1
            elif cnt%3== 2:
                x-=1
                y-=1
            arr[x][y] = num
            num+=1
        cnt+=1
    print(arr)
    for i in range(n):
        for j in range(n):
            if arr[i][j]!=0:
                answer.append(arr[i][j])
    print(answer)
    return answer
