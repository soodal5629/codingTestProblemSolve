def solution(info, query):
    answer = []
    arr = []
    for i, v in enumerate(query):
        query[i]= query[i].replace("and ", "")
        temp = query[i].split()
        temp[-1] = int(temp[-1])
        arr.append(temp)
    arr2= []
    for  i, v in enumerate(info):
        temp = info[i].split()
        temp[-1] = int(temp[-1])
        arr2.append(temp)

    for i in arr:
        cnt = 0
        for index, k in enumerate(info):
            flag = True
            for j in range(len(i)):
                if j!=len(i)-1 and i[j] not in k:
                    if i[j] != "-":  
                        flag = False
                if j == len(i)-1:
                    if arr2[index][-1]<i[j]:   
                        flag = False
            if flag == True:
                cnt+=1
        answer.append(cnt)
    return answer
