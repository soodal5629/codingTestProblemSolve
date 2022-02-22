from itertools import combinations
def solution(nums):
    answer = 0
    l = list(combinations(nums,3))
    for i in l:
        s = sum(i)
        cnt = 0
        if s == 2 or s==3 or s==5: answer+=1
        else:
            for j in range(2, (s//2)+1):
                if s%j == 0:
                    cnt +=1
                    break
            if cnt == 0: answer +=1 
    return answer
