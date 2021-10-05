n=int(input())
array = list(map(int, input().split()))
equation = list(map(int, input().split()))

global max_num, min_num
max_num = -1e9
min_num = 1e9

def bfs(step, value, array, plus, minus, mul, divi):
	global max_num, min_num
	if step == n:
		max_num = max(max_num, value)
		min_num = min(min_num, value)
		return
	if plus>0:
		bfs(step+1, value+array[step], array, plus-1, minus, mul, divi)
	if minus>0:
		bfs(step+1, value-array[step], array, plus, minus-1, mul, divi)
	if mul>0:
		bfs(step+1, value*array[step], array, plus, minus, mul-1, divi)
	if divi>0:
		bfs(step+1, int(value/array[step]), array, plus, minus, mul, divi-1)
		
bfs(1, array[0], array, equation[0], equation[1],equation[2],equation[3])
print(max_num)
print(min_num)
