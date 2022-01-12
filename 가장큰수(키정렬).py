def solution(numbers):
    answer = ''
    answer = ''
    numbers.sort(key = lambda x: str(x)*4, reverse = True) # sort -> key 이용, str으로 정렬해도 잘 정렬됨(사전순이기 때문)
    for i in numbers:
          answer += str(i)
    if answer[0] == "0": answer = '0'
        
    return answer
