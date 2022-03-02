def solution(nums):
    answer = 0
    num = len(nums)//2
    s=set(nums)
    if len(s) <= num: answer = len(s)
    else: answer = num
    return answer
