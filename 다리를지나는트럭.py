from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck = deque([0] * bridge_length)
    q = deque(truck_weights)
    s = 0 # 다리 위의 트럭 weight 합 
    while truck:
        if truck: 
            s-=truck.popleft()
        answer += 1
        if q:
            if (s + q[0])<= weight:
                temp = q.popleft()
                s += temp
                truck.append(temp)
            else:
                truck.append(0)
    return answer
