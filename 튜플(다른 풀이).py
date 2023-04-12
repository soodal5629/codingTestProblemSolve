def solution(s):
    answer = []
    arr = s[1:len(s)-1].split('}')
    arr.sort(key = lambda x:len(x))
    for i in arr:
        j = i.split(',')
        for k in j:
            if len(k) == 0: continue
            k = k.replace('{', '')
            if int(k) not in answer:
                answer.append(int(k))
    return answer
