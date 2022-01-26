def solution(brown, yellow):
    answer = []
    arr = []
    for i in range(1, yellow+1):
        if yellow % i== 0:
            if i>= (yellow//i): arr.append((i, yellow//i)) # 가, 세
    
    for i in arr:
        w, h = i
        if (w+2)*2 + (2*h) == brown:
            answer.append(w+2)
            answer.append(h+2)
            break
    return answer
