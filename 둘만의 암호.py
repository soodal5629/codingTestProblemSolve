def solution(s, skip, index):
    answer = ''
    arr = []
    for i in range(97, 123):
        if chr(i) in skip:
            continue
        arr.append(chr(i))
    for i in s:
        temp = arr.index(i) + index
        if temp >= len(arr):
            while temp >= len(arr): # 이 부분이 런타임에러 통과하는 핵심
                temp -= len(arr)
        answer += arr[temp]
    return answer
