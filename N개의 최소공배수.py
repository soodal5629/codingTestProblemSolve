from collections import deque
def gcd(a, b): # 두 수의 최대공약수(a<=b)
    while a!=0:
        r = b%a
        b = a
        a = r
    return b

def lcm(a, b): # 두 수의 최소공배수
    return a*b//gcd(a, b)
  
def solution(arr):
    answer = 1
    arr.sort()
    if len(arr) ==1: return arr[0]
    if 1 in arr: arr.remove(1)
    arr = deque(arr)
    while len(arr)>1:
        first = arr.popleft()
        sec = arr.popleft()
        temp = lcm(first, sec)
        arr.append(temp)
    answer = arr.pop()
    return answer
