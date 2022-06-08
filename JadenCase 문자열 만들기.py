def solution(s):
    arr = s.split()
    for i in range(len(arr)):
        arr[i] = arr[i].capitalize()
    temp = ''.join(arr)
    for i, v in enumerate(s):
        if v == " ":
            temp = temp[:i]+ ' ' + temp[i:]
    return temp
