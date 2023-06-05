def solution(sizes):
    answer = 0
    maxi = -1e9
    for i in sizes:
        a, b = i
        maxi = max(maxi, max(a, b))
    mini = min(sizes[0][0], sizes[0][1])
    for i in sizes:
        a, b = i
        temp = min(a, b)
        mini = max(mini, temp)
    answer = maxi * mini
    return answer
