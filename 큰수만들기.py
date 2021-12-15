from collections import deque
def solution(number, k):
    answer = ''
    n = len(number)-k
    stack = deque() 
    arr = list(map(int, number))
    arr = deque(arr)
    while len(arr)>0:
        if len(stack)==0:
            stack.append(arr.popleft())
            continue
        else:
            top = stack[-1]
            push_value = arr.popleft()
            if top < push_value:
                while top<push_value and k>0:
                    stack.pop()
                    k-=1
                    if len(stack)>0: top = stack[-1]
                    else: break
                stack.append(push_value)
            else: stack.append(push_value)
    if len(stack)>n:
        while len(stack) != n:
            stack.pop()
    if stack[0] == 0:
        answer = '0'
    else:
        for i in stack:
            answer += str(i)
    return answer
