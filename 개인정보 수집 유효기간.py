from collections import defaultdict
def change(date, term, dic):
    y, m, d = date.split('.')
    if dic[term] > 12:
        y = int(y) + dic[term] // 12
        m = int(m) + dic[term] % 12
    else: m = int(m) + dic[term]
    if m > 12:
        m -= 12
        y = int(y)+1
    d = int(d) -1
    if d == 0:
        if m == 1:
            m = 12
            y -=1
        m-=1
        d = 28
    return int(y),m,int(d)

def solution(today, terms, privacies):
    answer = []
    dic= defaultdict(int)
    for i in terms:
        word, term = i.split(' ')
        dic[word] = int(term)
    y, m, d = today.split('.')
    y = int(y)
    m = int(m)
    d = int(d)
    for i,v in enumerate(privacies):
        date, term = v.split(' ')
        a,b,c = change(date, term, dic)
        if a<y:
            answer.append(i+1)
            continue
        elif y<a: continue
        else:
            if b  == m: 
                if c < d:
                    answer.append(i+1)
            elif b < m: 
                answer.append(i+1)
    return answer
