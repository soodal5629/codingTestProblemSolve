def solution(cards1, cards2, goal):
    answer = ''
    index1= index2 = -1
    for i, v in enumerate(goal):
        if v in cards1:
            temp = cards1.index(v)
            if temp == index1+1: 
                index1 = temp
            else: 
                answer = 'No'
                break
        elif v in cards2:
            temp2 = cards2.index(v)
            if temp2 == index2+1:
                index2 = temp2
            else: 
                answer = 'No'
                break
        else: return 'No'
    if answer != 'No': answer = 'Yes'
    return answer
