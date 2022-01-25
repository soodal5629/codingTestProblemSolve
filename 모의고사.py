def solution(answers):
    answer = []
    first = ([1,2,3,4,5]*10000)[:10000]
    second =([2,1,2,3,2,4,2,5]*10000)[:10000]
    third = ([3,3,1,1,2,2,4,4,5,5]*10000)[:10000]
    cnt1=  0
    cnt2 = 0
    cnt3= 0
    for i,value in enumerate(answers):
        if value == first[i]: cnt1 +=1
        if value == second[i]: cnt2 +=1
        if value == third[i]: cnt3 +=1
    arr = [(cnt1,1), (cnt2,2), (cnt3,3)]
    maxi = max(arr)
    
    for i in arr:
        if maxi[0] == i[0]:
            answer.append(i[1])

    return answer
