def solution(people, limit):
    answer = 0
    left = 0
    right = len(people)-1
    people.sort()

    while left<=right:
        if people[right] + people[left]<=limit:
            right -=1
            left +=1
            answer+=1
        elif left == right:
            answer+=1
            break
        else:
            answer +=1
            right -=1
    return answer
