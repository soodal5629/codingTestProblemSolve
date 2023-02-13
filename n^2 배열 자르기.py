def solution(n, left, right):
    answer = []
    for i in range(left, right+1):
        a, b = divmod(i, n)
        temp = max(a, b) + 1
        answer.append(temp)
    return answer
