from collections import deque
def solution(ingredient):
    answer = 0
    d = deque()
    s = [0,1,3,2,1] # 스택이니까 거꾸로 뒤집은 다음 pop한 애들이랑 비교
    for i in ingredient:
        d.append(i)
        if len(d) > 3:
            flag = True
            for j in range(1,5):
                if s[j] != d[-j]:
                    flag = False
                    break
            if flag:
                answer+=1
                for j in range(0,4):
                    d.pop()
    return answer
