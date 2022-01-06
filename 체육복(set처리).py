def solution(n, lost, reserve):
    answer = 0
    
    s = set(lost) & set(reserve) # 교집합(여벌가진애가 잃어버렸을 경우)
    r = set(reserve) - s
    l = set(lost) - s
    for i in sorted(r): # 정렬해서 앞부터 살핌 --> 복잡도 O(n log n)
        if i-1 in l:
            l.remove(i-1)
        elif i+1 in l:
            l.remove(i+1)
    answer = n- len(l)
    return answer
