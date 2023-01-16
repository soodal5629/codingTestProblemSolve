def solution(n):
    answer = ''
    d = [0] * (n+1)
    if n == 1 or n == 2 : return str(n)
    d[1] = 1
    d[2] = 2 
    d[3] = 4
    if n == 3: return str(4)
    for i in range(4, len(d)):
        if i % 3 != 0:
            d[i] = str(d[i//3]) + str(d[i%3])
        else:
            d[i] = str(d[i//3 - 1]) + str(4)
    answer = d[n]
    return answer
