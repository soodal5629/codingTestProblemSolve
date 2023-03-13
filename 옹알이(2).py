def solution(babbling):
    answer = 0
    for i in babbling:
        s = i
        temp = 0
        flag= True
        while flag and len(s)>0:
            if s.startswith('aya') and temp!= 1:
                temp = 1
                s = s[3:]
            elif s.startswith('ye') and temp!= 2:
                temp = 2
                s = s[2:]
            elif s.startswith('woo') and temp!= 3:
                temp = 3
                s = s[3:]
            elif s.startswith('ma') and temp!= 4:
                temp = 4
                s = s[2:]
            else: break
        if len(s) == 0 and flag: answer+=1
    return answer
