def find(sticker):
    arr = [i for i in sticker]
    n = len(arr) - 1
    arr[n-2] += arr[n]
    for i in range(n-3, -1, -1):
        arr[i] += max(arr[i+2], arr[i+3])
    return max(arr)
def solution(sticker):
    answer = 0
    n = len(sticker)
    if len(sticker) <=3 : return max(sticker)
    a = find(sticker[:n-1])
    b = find(sticker[1:])
    answer = max(a, b)
    return answer
