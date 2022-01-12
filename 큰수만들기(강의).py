def solution(number, k):
    answer = ''
    temp = []
    for i, value in enumerate(number):
        while k>0 and len(temp)>0 and temp[-1]<value:
            temp.pop()
            k-=1
        temp.append(value)
    
    answer = ''.join(temp)
    if k>0: answer = answer[:k+1] # 이미 정렬되어서 k가 모두 감소되지 않았을때는 k만큼 끝에서부터 잘라줘야함
    return answer
