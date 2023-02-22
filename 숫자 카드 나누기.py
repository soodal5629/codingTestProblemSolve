def gcd(a,b):
    while b > 1:
        if a % b == 0: return b
        a, b = b, a % b
    return b
def divideNotALl(arr, n):
    for i in arr:
        if i % n == 0: return False
    return True

def solution(arrayA, arrayB):
    answer = 0
    n1 = arrayA[0]
    n2 = arrayB[0]
    
    for i in range(1, len(arrayA)):
        n1 = gcd(n1, arrayA[i])
    flag1 = divideNotALl(arrayB, n1)
    if flag1 == False: n1 = 1
    else: answer = n1
    for i in range(1, len(arrayB)):
        n2 = gcd(n2, arrayB[i])
    flag2 = divideNotALl(arrayA, n2)
    if flag2 == False: n2 = 1
    else: answer = max(answer, n2)
    
    if answer == 1: answer = 0
    return answer
