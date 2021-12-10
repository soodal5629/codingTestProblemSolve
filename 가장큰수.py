def solution(numbers):
    answer = ''
    arr =  []
    for i in numbers:
        temp = -1
        if len(str(i))<4:
            temp = str(i)*4
        else: temp = str(i)
        arr.append((int(temp[:4]), i))
    arr = sorted(arr, key=lambda x:-x[0])
    
    for i in arr:
        answer += str(i[1])
    if answer[0] == '0': answer = '0'
    return answer
