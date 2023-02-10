def add10(s):
    [h, m] = s.split(':')
    m = int(h) * 60 + int(m)
    return m

def solution(book_time):
    answer = 0
    q = []
    book_time.sort(key = lambda x : x[0])
    for i, v in enumerate(book_time):
        q.sort()
        if len(q) == 0 :
            start, end = v
            if i == 0: answer+=1
            end = add10(end) + 10
            q.append(end)
        else:
            cnt = 0
            for index, value in enumerate(q):
                now = value
                start, end = v
                start = add10(start)
                if start >= now:
                    q[index] = add10(end)+10
                    cnt +=1
                    break
            if cnt == 0:
                q.append(add10(end)+10)
                answer+=1
                
    return answer
