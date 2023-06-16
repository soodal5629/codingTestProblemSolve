def classify(s):
    header = number = tail = ''
    i = 0
    n_index = 0
    flag = True
    while i < len(s):
        if s[i].isdigit():
            if n_index == 0 or abs(n_index - i) == 1:
                number += s[i]
                n_index = i
            elif abs(n_index - i) != 1:
                tail+=s[i]
                flag = False
        else:
            if flag and n_index == 0:
                header += s[i]
            else:
                tail+=s[i]
        i+=1
    return header,number,tail
def solution(files):
    answer = []
    arr = []
    for i in range(len(files)):
        temp = [i]
        a,b,c = classify(files[i])
        temp.append(a)
        temp.append(b)
        temp.append(c)
        arr.append(temp)
    arr.sort(key=lambda x:(x[1].lower(), int(x[2]), x[0]))
    for i in arr:
        answer.append(''.join(i[1:]))
    return answer
