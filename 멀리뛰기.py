def solution(n):
    answer = 0
    arr = [0] * (n+2)
    arr[0] =0
    arr[1] = 1
    arr[2] = 2
    if n>2:
        for i in range(3,n+1):
            arr[i] = (arr[i-1] + arr[i-2])%1234567
    answer = arr[n]
    return answer
