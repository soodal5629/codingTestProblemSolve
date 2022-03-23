def solution(d, budget):
    answer = 0
    d.sort()
    temp = 0
    for i in d:
        if temp+i>budget: break
        else:
            temp +=i
            answer +=1
    return answer
