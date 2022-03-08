def solution(record):
    answer = []
    d = {}
    for i in record:
        temp = i.split(" ")
        if temp[0] == 'Enter' or temp[0] == 'Change': d[temp[1]] = temp[2]
    for i in record:
        arr = i.split(" ")
        if arr[0] == 'Enter':
            answer.append(d[arr[1]]+'님이 들어왔습니다.')
        elif arr[0] == 'Leave':
            answer.append(d[arr[1]]+'님이 나갔습니다.')  
    
    return answer
