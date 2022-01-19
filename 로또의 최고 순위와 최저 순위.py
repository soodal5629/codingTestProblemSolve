def solution(lottos, win_nums):
    answer = []
    maxi = 0
    mini = 0
    win_d = {}
    for i in win_nums:
        win_d[i] = 1

    for i in lottos:
        if i == 0:
            maxi +=1
        if i in win_d and win_d[i] == 1:
            maxi +=1
            mini +=1
    rank = [6,5,4,3,2]
    print(maxi, mini)
    flag = False
    flag2 = False
    for i in range(len(rank)):
        if rank[i] == mini:
            mini = i+1
            flag = True
            break
    for i in range(len(rank)):
        if rank[i] == maxi:
            maxi = i+1
            flag2 = True
            break
    if flag == False:
        mini = 6
    if flag2 == False:
        maxi = 6
    
    answer.append(maxi)
    answer.append(mini)
    print(answer)
    return answer
