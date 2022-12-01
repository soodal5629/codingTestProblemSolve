def solution(topping):
    answer = 0
    part1 = set()
    part2 = set()
    count1 = []
    count2 = []
    for i in topping:
        part1.add(i)
        count1.append(len(part1))
    for i in topping[::-1]:
        part2.add(i)
        count2.append(len(part2))
    count2 = count2[::-1]  
    for i in range(len(count2)-1):
        if count1[i] == count2[i+1]: answer+=1
    return answer
