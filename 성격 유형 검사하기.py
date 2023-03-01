from collections import defaultdict
def solution(survey, choices):
    answer = ''
    d = defaultdict(list)
    d[1] = ['R', 'T']
    d[2] = ['C', 'F']
    d[3] = ['J', 'M']
    d[4] = ['A', 'N']
    d2 = defaultdict(int)
    temp = 'RTCFJMAN'
    for i in temp:
        d2[i] = 0
    for i in range(len(survey)):
        a, b = survey[i]
        score = choices[i]
        if score > 4:
            d2[b] += score-4
        elif score < 4:
            d2[a] += 4-score
    for i in range(1, 5):
        a,b = d[i]
        value1 = d2[a]
        value2 = d2[b]
        if value1 > value2: 
            answer += a
        elif value1 < value2: 
            answer += b
        else:
            if a < b:
                answer += a
            else:
                answer+=b
    return answer
