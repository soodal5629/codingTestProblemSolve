import itertools
def solution(numbers):
    answer = 0
    arr = []
    for i in numbers:
          arr.append(i)
    s = set()
    for i in range(1,len(arr)+1):
        s.update(list(map(''.join, itertools.permutations(arr, i))))

    for j in s:
        if j[0] == '0': j = '0'
        j = int(j)
        flag = False
        if j == 0 or j == 1: continue
        elif j==2 or j==3 or j==5: answer +=1
        else:
            for k in range(2, j):
                if j%k ==0:
                    flag = True
                    break
            if flag == False:
                answer += 1
    return answer
