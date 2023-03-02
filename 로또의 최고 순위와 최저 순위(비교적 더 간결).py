def solution(lottos, win_nums):
    answer = []
    
    if lottos.count(0) == 6: return [1,6]
    cnt = 0
    zero = lottos.count(0)
    for i in range(len(lottos)):
        if lottos[i] in win_nums: cnt+=1
    if zero > 0:
        answer = [7 - (cnt + zero), 7 - cnt]
    elif cnt > 0: answer = [7-(cnt), 7-(cnt)]
    else: answer = [6,6]

    return answer
