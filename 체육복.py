def solution(n, lost, reserve):
    answer = 0
    mini = n - len(lost) # 최솟값 
    answer = mini
    reverse_flag = [True] * (n+1)
    lost_flag = [True] * (n+1)
    lost.sort()
    reserve.sort()
    for i in lost: #여벌 가져온애가 지꺼 잃어버렸을 때
        if reserve.count(i)==1:
            reverse_flag[i] = False
            lost_flag[i] = False
            answer += 1
    for i in lost:
        if lost_flag[i] == False: continue
        for j in reserve:
            if abs(j-i) == 1 and reverse_flag[j]:
                reverse_flag[j] = False
                lost_flag[i] = False
                answer += 1
                break
    print(answer)
    return answer
