def solution(sequence, k):
    answer = []
    if k in sequence:
        return [sequence.index(k), sequence.index(k)]
    l = 0
    r = 1
    n = len(sequence)
    temp = sequence[0]
    s = 1e9
    while l<r and r < n:
        temp += sequence[r]
        if temp == k:
            if s > (r - l + 1):
                s = (r-l+1)
                answer = [l, r]
        elif temp > k:
            temp -= sequence[l]
            temp -= sequence[r]
            l +=1
            continue
        r+=1        
    return answer
