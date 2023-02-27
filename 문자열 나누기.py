from collections import deque
def solution(s):
    answer = 0
    x = s[0]
    d = deque()
    d.append(x)
    cnt1 = 1
    cnt2 = 0
    for i in range(1, len(s)):
        if d:
            top = d[0]
            if top == s[i]:
                cnt1+=1
            else:
                cnt2+=1
                if cnt1 == cnt2:
                    answer+=1
                    cnt2= 0
                    d.clear()
        else:
            d.append(s[i])
            cnt1 = 1
    if d: answer+=1
    return answer

solution('banana')
