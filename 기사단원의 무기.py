import math
def solution(number, limit, power):
    answer = 0
    arr = []
    for i in range(1, number+1):
        cnt = 0
        for j in range(1, int(math.sqrt(i))+1):
            if j*j == i: cnt+=1  
            elif i % j == 0: cnt+=2
            if cnt > limit:
                cnt = power
                break
        answer += cnt
    return answer
