def solution(a, b, n):
    answer = 0
    temp = 0
    while n >= a:
        x, y = divmod(n, a)
        answer += (x * b)
        n = x * b # 솔직히 이해 잘 안됨,, 힌트보고 넣음
        if y != 0: temp += y
        if n < a and temp > 0:
            n += temp
            temp = 0 
    return answer
