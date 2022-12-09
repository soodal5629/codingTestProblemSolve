def divideAll(arr, n):
    temp = n
    while n > 1 :
        for i in range(0,len(arr)):
            if i == len(arr)-1 and arr[i]%n == 0: return n
            if arr[i] % n == 0:
                continue
            else:
                if temp == n and n%2 == 0 : 
                    n = n//2
                else: 
                    n -=1
                break
    return n
def divideNotALl(arr, n):
    for i in arr:
        if i % n == 0: return False
    return True
def solution(arrayA, arrayB):
    answer = 0
    a = arrayA[0]
    b = arrayB[0]
    n1 = divideAll(arrayA, a)
    if n1 != 1:
        flag1 = divideNotALl(arrayB, n1)
        if flag1 == False: n1 = 1
    n2 = divideAll(arrayB, b)
    if n2 != 1:
        flag2 = divideNotALl(arrayA, n2)
        if flag2 == False: n2 = 1
    answer = max(n1, n2)
    if answer == 1: answer = 0
    return answer
