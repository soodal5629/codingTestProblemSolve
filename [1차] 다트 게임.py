from collections import deque
def solution(dartResult):
    answer = 0
    d = deque()
    temp = 0
    m = ''
    for i in dartResult:
        if i.isdigit(): m += i
        elif i == 'S':
            d.append(int(m))
            m = ''
        elif i == 'D':
            d.append(int(m)**2)
            m = ''
        elif i == 'T':
            d.append(int(m)**3)
            m = ''
        elif i == '#':
            d.append(-d.pop())
        elif i == '*':
            temp2 = 0
            arr = deque()
            # 2배 해줄때 한번에 연산하고 2배해서 넣어주면 2문제 통과못함 => 각 원소를x2 해준다음 다시 d에 넣어줘야 테스트 통과함
            for j in range(2):
                if d:.
                    arr.appendleft(2*d.pop())
            for j in arr:
                d.append(j)
    for i in d:
        answer+=i
    return answer
