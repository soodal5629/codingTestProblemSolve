
def solution(participant, completion):
    answer = ''
    part = dict() # 파이썬에서는 Dictionary라는 자료구조를 통해 해시 제공 => Dictionary는 dict클래스에 구현되어 있음
    for i in participant:
        if i in part:
            part[i] +=1
        else:
            part[i] = 1
    for i in completion:
        part[i] -= 1
    for i in part:
        if part[i] != 0:
            answer = i 
    return answer
  
