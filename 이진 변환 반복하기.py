def binary(num):
    s = ""
    while num>1:
        temp = num%2
        num = num//2
        s += str(temp)
    s+=str(num)
    s[::-1]
    return s
def solution(s):
    answer = []
    cnt = 0
    cnt2 = 0
    while s!="1":
        cnt+=1
        cnt2 += s.count("0")
        s = s.replace("0", "")
        num = len(s)
        s = binary(num)
    
    answer.append(cnt)
    answer.append(cnt2)
    return answer
