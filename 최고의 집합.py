def solution(n, s):
    answer = []
    if n >= s: return [-1]
    a = s//n
    answer = [a] * n
    index = n-1
    temp = sum(answer)
    while temp < s:
        temp +=1
        answer[index] +=1
        if index > 0 : index -=1
        else: index = n-1
    return answer
