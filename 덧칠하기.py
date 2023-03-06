def solution(n, m, section):
    answer = 1
    now = section[0] + m -1
    for i in section:
        if now < i:
            answer+=1
            now = i+ m -1
    return answer
