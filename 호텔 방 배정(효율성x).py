def solution(k, room_number):
    answer = []
    d = {}
    for i,value in enumerate(room_number):
        if value not in d: d[value] = i+1
        else:
            j = value+1
            while True:
                if j in d: j+=1
                else:
                    d[j] = i+1
                    break
    temp=[]
    for i in d.keys():
        answer.append(i)
    return answer
