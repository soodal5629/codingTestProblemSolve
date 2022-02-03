from collections import deque
def solution(begin, target, words):
    answer = 0
    q=deque()
    d = {}
    for i in words:
        d[i] = 0
    for idx, i in enumerate(words):
        if i == begin: continue
        cnt = 0
        for j in range(len(i)):
            if i[j] != begin[j]:
                cnt +=1
        if cnt == 1: 
            q.append(i)
            words[idx] = ""
            d[i] += 1
        while q:
            s = q.popleft()
            if s == target: 
                break
            for idx, i in enumerate(words):
                cnt = 0
                for j in range(len(i)):
                    if i[j] != s[j]:
                        cnt +=1
                if cnt == 1:
                    q.append(i)
                    words[idx] = ""
                    d[i] = d[s]+1
    if target in d:
        answer = d[target]
    else: answer =0
    return answer
