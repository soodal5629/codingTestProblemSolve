def find(n):
    res = 1
    for i in range(1, n//2+1):
        if n%i == 0: res+=1
    return res
def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        cnt = find(i)
        if cnt%2 == 0:
            answer += i
        else: answer -= i
    return answer
