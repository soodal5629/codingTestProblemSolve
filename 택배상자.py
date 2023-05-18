from collections import deque
def solution(order):
    answer = 0    
    arr = deque([i for i in range(1, len(order)+1)])
    d = deque() # 임시 컨테이너
    index = 0
    for i in arr:
        j = order[index]
        if i == j:
            temp = i
            while temp == order[index]:
                answer+=1
                index+=1
                if index >= len(order): break
                if d:
                    temp = d.pop()
            d.append(temp)
        else:
            d.append(i)
    return answer
