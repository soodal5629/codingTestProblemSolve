def solution(land):
    answer = 0
    
    for i in range(1, len(land)):
        for j in range(4):
            temp = land[i][j]
            for k in range(4):
                if j != k:
                    land[i][j] = max(land[i][j], (land[i-1][k] + temp))
    answer = max(land[len(land)-1])

    return answer
