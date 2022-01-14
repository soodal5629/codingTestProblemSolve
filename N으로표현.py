def solution(N, number):
    answer = 0
    s=list(set() for _ in range(9))
    for i in range(1, 9):
        s[i].add(int(str(N)*i))
    for i in range(1, 9):
        for j in range(1, i):
            for x in s[j]:
                for y in s[i-j]: 
                    s[i].add(x+y)
                    s[i].add(x-y)
                    s[i].add(x*y)
                    if y!=0: s[i].add(x//y)
        if number in s[i]: 
            answer = i
            break
    if answer == 0:
        answer = -1
    return answer
