def solution(key, lock):
	new_lock = [[0 for _ in range(len(key)*3)] for _ in range(len(key)*3)]
	len_lock = len(lock)
	len_key = len(key)
	for i in range(len_lock, len_lock*2):
		for j in range(len_lock, len_lock*2):
			new_lock[i][j] = lock[i-len_lock][j-len_lock]
	rotate_num = 0
	while(rotate_num<4):
		rotate_num +=1
		key = rotate(key)
		temp = new_lock
		for x in range(2*len_lock):
			for y in range(2*len_lock):
				for i in range(len_key):
					for j in range(len_key):
						print(x, y, i, j)
						new_lock[x+i][y+j] += key[i][j] 
				if sum_check(new_lock):	return True						
				for i in range(len_key):
					for j in range(len_key):
						new_lock[x+i][y+j] -=key[i][j]
	return False

def sum_check(temp):
	len_temp = len(temp)
	start = len_temp//3
	for i in range(start, 2*start):
		for j in range(start, 2*start):
			if temp[i][j] !=1: return False
	return True
	
def rotate(key):
	new_key=[[-1 for _ in range(len(key))] for _ in range(len(key))]
	for i in range(len(key)):
		for j in range(len(key)):
			new_key[j][len(key)-1-i] = key[i][j]
	return new_key

key = [[0,0,0],[1,0,0],[0,1,1]]
lock = [[1,1,1],[1,1,0],[1,0,1]]
print(solution(key, lock))
