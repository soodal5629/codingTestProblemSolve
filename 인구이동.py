from collections import deque
import sys

def push_city(city, min, max, i, j, visit):
	res = False
	dx = [-1,1,0,0]
	dy = [0,0,-1,1]
	mini_map = []
	q = deque()
	q.append((city[i][j], i, j))
	while(q):
		now, x, y = q.popleft()
		visit[x][y] = True
		mini_map.append((now, x, y))
		for index in range(4):
			if x+dx[index]<0 or y+dy[index]<0 or x+dx[index]>=n or y+dy[index]>=n: continue
			else:
				if visit[x+dx[index]][y+dy[index]]: continue
				if abs(city[x][y]-city[x+dx[index]][y+dy[index]])>=min and abs(city[x][y]-city[x+dx[index]][y+dy[index]])<=max:
					visit[x+dx[index]][y+dy[index]] = True
					q.append((city[x+dx[index]][y+dy[index]], x+dx[index], y+dy[index]))			
					res = True
	part_sum = 0
	mini_map_count = 0
	#print("mini_map: ", mini_map)
	for mini_x in mini_map:
		part_sum += mini_x[0]
		mini_map_count+=1
	for _ in range(mini_map_count):
		value, a, b = mini_map.pop()			
		city[a][b] = part_sum//mini_map_count
	return visit, city, res

def find_neighbr(city, min, max):
	n = len(city)
	day = 0
	flag = True
	visit = [[False for cols in range(n)] for rows in range(n)]
	while flag:
		# one cycle
		change = False
		count = 0
		for i in range(n):
			for j in range(n):
				if visit[i][j]: continue
				visit, city, res = push_city(city, min, max, i, j, visit)
				if res: count+=1
		if count>0:
			day+=1
			visit = [[False for cols in range(n)] for rows in range(n)]
		else:
			flag = False
		
	print(day)
	#print(city)
            
n, min, max = map(int, sys.stdin.readline().split())
city = []
for i in range(n):
	city.append(list(map(int, input().split())))
find_neighbr(city, min, max)
