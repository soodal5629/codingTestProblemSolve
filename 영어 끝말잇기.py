def solution(n, words):
    answer = []
    d = {}
    d[words[0]]=1
    for i in range(1,len(words)):
        word = words[i-1]
        next = words[i]
        if word[-1] != next[0] or word ==next:
            answer.append(i%n+1)
            answer.append(i//n+1)
            break
        if next not in d:
            d[next] = 1
        else:
            answer.append(i%n+1)
            answer.append(i//n+1)
            break
    if len(answer) == 0:
        answer.append(0)
        answer.append(0)
    
    return answer
