from collections import deque
def change(s):
    if str(type(s)) == "<class 'int'>": return s
    h, m = s.split(':')
    return int(h) * 60 + int(m)
def solution(plans):
    answer = []
    d = deque()
    plans.sort(key = lambda x:x[1])
    arr = deque(plans)
    d.append(arr.popleft())
    while d:
        if d:
            now = d.pop()
            sub, time, take = now
            take = int(take)
            time = change(time)
            if arr: 
                new = arr.popleft()
                s, time2, take2 = new
                time2 = change(time2)
                extra = time2 - time
                if extra < take:
                    take -= extra
                    d.append([sub, time, take])
                    d.append(new)
                else:
                    answer.append(sub)
                    if take < extra:
                        extra -= take
                        while d and extra > 0:
                            temp = d.pop()
                            temp_s, temp_t, temp_take = temp
                            temp_take = int(temp_take)
                            if extra < temp_take:
                                temp_take -= extra
                                d.append([temp_s, temp_t, temp_take])
                                #d.append(new)
                                break
                            else:
                                extra -= temp_take
                                answer.append(temp_s)
                        d.append(new)
                    else:
                        d.append(new)    
            else:
                answer.append(sub)
    
    return answer
