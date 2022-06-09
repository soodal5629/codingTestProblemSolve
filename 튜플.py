def solution(s):
    answer = []
    arr = []
    temp = []
    num = ''
    temp = s[1:len(s)-1].split("}")
    for i in range(len(temp)):
        if len(temp[i]) == 0: continue
        temp2 = temp[i].split(',')    
        arr2=[]
        for j in range(len(temp2)):
            word= temp2[j]
            if word == '': continue
            if '{' in word:
                word = word.replace("{", '')
                temp2[j] = word
            arr2.append(int(word))
        arr.append(arr2)

    arr.sort(key=lambda x:len(x))
    for i in arr:
        for j in i:
            if j not in answer:
                answer.append(j)
    return answer
