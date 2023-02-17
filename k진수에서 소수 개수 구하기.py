def trans(n, k):
    temp = ''
    while n > 0:
        a, b = divmod(n, k)
        temp += str(b)
        n = a
    temp = temp[::-1]
    return temp
def find(n):
    if n== 1: return 0
    if n==2 or n==3 or n==5: return 1
    flag = True
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            flag = False
            break
    if flag: return 1
    else: return 0

def solution(n, k):
    answer = 0
    num = str(n)
    if k != 10:
        num = trans(n, k)
    arr = num.split('0')
    for i in arr:
        if i=='': continue
        answer += find(int(i))
    return answerdef trans(n, k):
    temp = ''
    while n > 0:
        a, b = divmod(n, k)
        temp += str(b)
        n = a
    temp = temp[::-1]
    return temp
  
def find(n):
    if n== 1: return 0
    if n==2 or n==3 or n==5: return 1
    flag = True
    for i in range(2, int(n**0.5)+1): # 제곱근 말고 n//2로 하면 1번문제만 시간초과 함, 소수는 앞으로 제곱근으로 범위를 잡아야 할 듯 싶다.
        if n%i == 0:
            flag = False
            break
    if flag: return 1
    else: return 0

def solution(n, k):
    answer = 0
    num = str(n)
    if k != 10:
        num = trans(n, k)
    arr = num.split('0')
    for i in arr:
        if i=='': continue
        answer += find(int(i))
    return answer
