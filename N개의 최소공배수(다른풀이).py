def solution(arr):
    answer = 1
    arr.sort()
    m = max(arr)
    while True:
        flag = True
        for i in arr:
            if m % i != 0:
                flag = False
                break
        if flag == False: m+=max(arr)
        else: 
            answer = m
            break
    print(answer)
    return answer
