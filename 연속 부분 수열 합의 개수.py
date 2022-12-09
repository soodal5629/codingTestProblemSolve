def solution(elements):
    answer = 0
    s = set(elements)
    for i in range(2, len(elements)+1):
        arr = elements + elements[0:i-1]
        for j in range(0, len(arr) - i+1):
            s.add(sum(arr[j:j+i]))
    answer +=len(s)
    return answer
