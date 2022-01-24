def solution(citations):
    answer = 0
    citations.sort()
    for i, value in enumerate(citations):
        temp = len(citations)-i
        if i<=value and value>=temp:
            answer = max(answer, temp)  
    return answer
