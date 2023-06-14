from collections import deque
def binary(l, n):
    s = ''
    while n > 0:
        s += str(n%2)
        n = n//2
    s = s[::-1]
    if len(s) < l:
        s = '0' * (l-len(s)) + s
    return s
def solution(n, arr1, arr2):
    answer = []
    a = []
    b = []
    for i in range(len(arr1)):
        s = binary(n, arr1[i])
        s2 = binary(n, arr2[i])
        a.append(list(s))
        b.append(list(s2))
    for i in range(n):
        temp = ''
        for j in range(n):
            if a[i][j] == '0' and b[i][j] == '0':
                temp += ' '
            else:
                temp += '#'
        answer.append(temp)
    return answer
