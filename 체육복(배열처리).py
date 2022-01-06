def solution(n, lost, reserve):
    answer = 0
    
    array = [1] * (n+2) # 0번과 n+1번 계산할때 용이하라고
    for i in reserve:
        array[i] +=1
    for i in lost:
        array[i] -=1
    for i in range(1, n+2):
        if array[i]>1 and array[i-1]==0:
            array[i] -=1
            array[i-1] +=1
        elif array[i]>1 and array[i+1] ==0:
            array[i] -=1
            array[i+1] +=1
    for i in range(1, n+1):
        if array[i] >0:
            answer+=1
    return answer
