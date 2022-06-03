def solution(n):
    answer = 1
    index = (n//2)+2
    for i in range(1, index):
        temp = 0
        for j in range(i, index):
            temp+=j
            if temp == n:
                answer+=1
                break
            if temp>n:
                break
    if n == 1 or n==2: answer = 1 
    return answer
