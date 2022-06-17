def trit(n):
    d = []
    while n>0:
        d.append(n%3)
        n = n//3
    return d
def solution(n):
    answer = 0
    arr = trit(n)
    temp = 1
    for i in range(len(arr)-1, -1,-1):
        answer += arr[i] * temp
        temp *= 3
    return answer
