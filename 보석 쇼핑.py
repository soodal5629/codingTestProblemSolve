from collections import defaultdict
def solution(gems):
    answer = [0,0]
    n = len(set(gems))
    l = r = 0
    d = defaultdict(int)
    d[gems[0]] = 1
    short = len(gems)+1 # +1 안해주면 통과 못함,,
    while l < len(gems) and r <len(gems) and l <= r:
        if len(d) == n:
            if short > (r - l + 1):
                short = r - l +1
                answer = [l, r]
            d[gems[l]] -= 1
            if d[gems[l]] == 0:
                del d[gems[l]]
            l += 1
        else:
            r += 1
            if r < len(gems):
                d[gems[r]] +=1
                
    answer = [answer[0]+1, answer[1]+1]
    return answer
