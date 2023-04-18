import math
def solution(r1, r2):
    answer = 0
    # x축 혹은 y축 위에 점이 있을 경우
    for i in range(r1, r2+1):
        answer +=4
    
    temp1 = r1**2
    temp2 = r2**2
    cnt = 0
    for i in range(1, r2):
        n = (i**2)
        miny = 1
        if temp1 -n >= 0:
            miny = math.ceil(math.sqrt(temp1 - n))
        maxy = math.floor(math.sqrt(temp2 - n))
        if miny == 0: miny = 1
        cnt += (maxy - miny + 1)
    answer += (4*cnt)    
    return answer
