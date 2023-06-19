from collections import deque
def solution(cacheSize, cities):
    answer = 0
    d = deque()
    if cacheSize == 0: return 5*len(cities)
    for i in range(len(cities)):
        temp = cities[i].lower()
        if temp in d:
            d.remove(temp)
            d.append(temp)
            answer+=1
        else:
            if d and len(d) >= cacheSize: d.popleft()
            d.append(temp)
            answer+=5
    return answer
