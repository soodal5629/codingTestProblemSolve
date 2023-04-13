one = zero =0
def find(x, y, arr, n):
    if n < 1: return
    a = b= 0
    for i in range(x, x+n):
        for j in range(y, y+n):
            if arr[i][j] == 1: a+=1
            else: b+=1
    if a== 0 and b>0:
        global zero
        zero+=1
        return
    elif a >0 and b == 0:
        global one
        one+=1
        return
    else:
        find(x,y,arr, n//2)
        find(x+(n//2),y,arr, n//2)
        find(x,y+(n//2),arr, n//2)
        find(x+(n//2),y+(n//2),arr, n//2)

def solution(arr):
    answer = []
    n = len(arr) // 2
    a = b= 0
    # 리스트 내 모든 요소가 1로만 이루졌늕지, 0으로만 이루어졌는지 확인 => 이거 안해주면 10번 테케 통과 못함
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == 0: b+=1
            else: a+=1
    if a == len(arr) * len(arr): return [0, 1]
    if b == len(arr) * len(arr): return [1, 0]
  
    find(0,0,arr, n)
    find(n,0,arr, n)
    find(0,n,arr, n)
    find(n,n,arr, n)
    global one
    global zero
    answer = [zero, one]
    return answer
