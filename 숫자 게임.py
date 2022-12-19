def solution(A, B):
    answer = 0
    A.sort(reverse=True)
    B.sort(reverse=True)
    index = 0
    for i in A:
        if i >= B[index]:
            continue
        else: 
            index+=1
            answer+=1
    return answer
