def solution(arr):
    answer = []
    for i, v in enumerate(arr):
        if i == 0:
            answer.append(v)
            continue
        top = answer[-1]
        if top == v:
            continue
        else:
            answer.append(v)
    return answer
