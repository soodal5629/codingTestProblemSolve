from collections import deque
def solution(priorities, location):
    answer = 0
    arr = deque()
    for i in range(len(priorities)):
        arr.append((priorities[i], i))
    while arr:
        top = arr.popleft()
        if arr and top[0] < max(arr)[0]:
            arr.append(top)
        else:
            answer+=1
            if top[1] == location:
                break
    return answer
