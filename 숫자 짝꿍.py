from collections import Counter
def solution(X, Y):
    answer = ''
    arr1= Counter(X)
    arr2= Counter(Y)
    arr = []
    for i in arr1.keys():
        if i in arr2.keys():
            temp = min(arr1[i], arr2[i])
            for j in range(temp):
                arr.append(int(i))
    arr.sort(reverse=True)
    if len(arr) == 0: return '-1'
    for i in arr:
        answer += str(i)
    if int(answer[0]) == 0: return '0' # 조건문을 int(answer) == 0 으로 하면 시간 초과 (answer가 엄청 긴가 봄..)
    return answer
