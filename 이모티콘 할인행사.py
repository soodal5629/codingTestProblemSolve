from itertools import product
def solution(users, emoticons):
    answer = [-1 , 0]
    discount = [10, 20, 30, 40]
    p = list(product(discount, repeat=len(emoticons)))
    for d in p:
        cnt = money = 0
        temp = 0
        for i in users:
            percent, limit = i
            temp2 = 0
            for k in range(len(d)):
                if d[k] < percent: continue
                temp2 += int(emoticons[k] - (emoticons[k] * d[k]/100))
            if temp2 >= limit:
                cnt +=1
                temp2 = 0
            temp+=temp2
        if cnt > answer[0]: 
            answer = [cnt, temp]
        elif cnt == answer[0] and temp >= answer[1]:
            answer = [cnt, temp]
    return answer
