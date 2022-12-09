from collections import deque
def solution(queue1, queue2):
    answer = 0
    d1 = deque(queue1)
    d2 = deque(queue2)
    s1 = sum(queue1)
    s2 = sum(queue2)
    while s1 >0 and s2 > 0:
        if s1 == s2:
            break
        if s1 > s2:
            temp1 = d1.popleft()
            d2.append(temp1)
            s1-=temp1
            s2+=temp1
        else:
            temp2 = d2.popleft()
            d1.append(temp2)
            s1+=temp2
            s2-=temp2
        answer+=1
        if answer > 600000:return -1 # 힌트 보고 넣었는데 이해는 안감..
        
    if s1 == 0 or s2 ==0 :answer = -1
    
    return answer
