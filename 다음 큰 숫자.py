def binary(n):
    s = ''
    while n>0:
        s+=str(n%2)
        n = n//2
    s= s[::-1]
    return s
def solution(n):
    answer = 0
    temp = n+1
    s = binary(n)
    cnt = s.count('1')
    cnt2 = -1
    while True:
        s2 = binary(temp)
        cnt2 = s2.count('1')
        if cnt == cnt2:
            answer = temp
            break
        else: temp+=1
    return answer
