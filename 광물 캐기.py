import heapq
def solution(picks, minerals):
    answer = 0
    arr = []
    cnt = sum(picks) * 5 # 곡괭이 수 - 테스트케이스 8번 때문에 신경써줘야 함
    for i in range(0, len(minerals), 5):
        temp = []
        if cnt > 0 and i+5 < len(minerals): 
            temp = minerals[i:i+5]
            cnt -=5
        elif cnt > 0 : 
            temp = minerals[i:]
            cnt -= len(temp)
        temp = [temp.count('diamond'), temp.count('iron'),temp.count('stone')]
        temp2 = [0,0,0]
        for j in range(3):
            if j == 0:
                temp2[0] = temp[0] + temp[1] + temp[2]
            elif j == 1:
                temp2[1] = temp[0] * 5 +temp[1] + temp[2]
            else:
                temp2[2] = temp[0]*25 + temp[1] *5 + temp[2]
        arr.append(temp2)
    arr.sort(key = lambda x:(-len(x), -x[2], -x[1], -x[0]))
    for i in arr:
        for j in range(len(picks)):
            if picks[j] <=0: continue
            picks[j]-=1
            answer += i[j]
            break
    return answer
