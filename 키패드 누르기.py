def find(num, x):
    res = abs(num - x)
    if res == 1 or res == 3: return 1
    else: return (res//3) + (res%3)
def solution(numbers, hand):
    answer = ''
    l = 10
    r = 12
    for num in numbers:
        if num in [1,4,7]:
            answer +='L'
            l = num
        elif num in [3,6,9]:
            answer+= 'R'
            r = num
        else:
            if num == 0: num = 11
            ld = find(num, l)
            rd = find(num, r)
            if ld < rd: 
                answer +="L"
                l = num
            elif ld > rd : 
                answer +="R"
                r = num
            else:
                if hand == 'right': 
                    answer+='R'
                    r = num
                else: 
                    answer+= "L"
                    l = num
    return answer
