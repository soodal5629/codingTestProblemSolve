from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    d = deque()
    d.append(truck_weights[0])
    t = deque(truck_weights[1:])
    weight -= d[0]
    while d:
        if t: now = t[0]
        else: now = 0
        if len(d) >= bridge_length: 
            top = d.popleft()
            weight += top
        if weight >= now :
            if t: 
                d.append(t.popleft())
                weight -= now
            else: d.append(0)
            answer+=1
        else:
            d.append(0)
            answer+=1
        if d.count(0) == bridge_length: break
    return answer+1
