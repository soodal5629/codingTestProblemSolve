def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        start, end, k = commands[i]
        temp = array[start-1:end]
        temp.sort()
        answer.append(temp[k-1])
    return answer
