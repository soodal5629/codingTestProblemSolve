def find(s, i):
    temp = 0
    index = 0
    next = index+i
    flag = False
    temp2 = 1
    while index < len(s):
        if s[index:next] == s[next:next+i]: 
            index = next
            next = index + i
            flag = True
            temp2+=1
            continue
        else:
            if flag: temp +=(len(str(temp2))+i)
            else: temp+=len(s[index:index+i])
            flag = False
            index  = next
            next = index +i
            temp2=1
    return temp
  
def solution(s):
    answer = len(s)
    n = len(s)
    for i in range(1, n//2+1):
        answer = min(answer, find(s, i))
    return answer
