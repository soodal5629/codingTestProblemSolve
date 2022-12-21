def solution(s):
    answer = ''
    arr = s.split(' ')
    mini = 1e9
    maxi = -1e9
    for i in arr:
        mini = min(mini, int(i))
        maxi = max(maxi, int(i))
    answer += str(mini)
    answer += ' ' 
    answer+= str(maxi)
    return answer
