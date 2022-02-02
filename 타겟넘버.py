global cnt
cnt = 0
def bfs(idx, value, numbers, target):
    if idx == len(numbers):
        if value == target:
            global cnt 
            cnt+=1
        return
    bfs(idx+1, value+numbers[idx],numbers,target)
    bfs(idx+1, value-numbers[idx], numbers, target)
def solution(numbers, target):
    answer = 0
    bfs(0,0,numbers, target)
    answer = cnt
    return answer
