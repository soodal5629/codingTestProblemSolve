from collections import deque

def push_city(city, min, max):
	pass
	
def find_neighbr(city, min, max):
	q = deque()
	n = len(city)
	dx = [-1,1,0,0]
	dy = [0,0,-1,1]
	mini_map = []
	day = 0
	flag = True
	visit = [[False for cols in range(n)] for rows in range(n)]
	count = 0
	count_x = 0 
	count_y = 0
	while flag:
		print(city)
		for i in range(n):
			count_x = i
			for j in range(n):
				count_y = j
				if visit[i][j]: continue
				for k in range(0,4): #동서남북 
					if i+dx[k]<0 or j+dy[k]<0 or i+dx[k]>=n or j+dy[k]>=n: continue
					if abs(city[i][j]-city[i+dx[k]][j+dy[k]])>=min and abs(city[i][j]-city[i+dx[k]][j+dy[k]])<=max:
						visit[i][j] = True
						q.append((city[i][j], i, j))
						count += 1
					if count>0: break
				if count>0: break
			if count>0: break
		
		if count>0:
			while(q):
				now, x, y = q.popleft()
				mini_map.append((now, x, y)) 
				visit[x][y] = True
				for index in range(4):
					if x+dx[index]<0 or y+dy[index]<0 or x+dx[index]>=n or y+dy[index]>=n: continue
					else:
						if visit[x+dx[index]][y+dy[index]]: continue
						if abs(city[x][y]-city[x+dx[index]][y+dy[index]])>=min and abs(city[x][y]-city[x+dx[index]][y+dy[index]])<=max:
							print("뿅")
							visit[x+dx[index]][y+dy[index]] = True
							q.append((city[x+dx[index]][y+dy[index]], x+dx[index], y+dy[index]))			
			part_sum = 0
			mini_map_count = 0
			print("mini_map: ", mini_map)
			for mini_x in mini_map:
				part_sum += mini_x[0]
				mini_map_count+=1
			for _ in range(mini_map_count):
				value, x, y = mini_map.pop()			
				city[x][y] = part_sum//mini_map_count
			print(part_sum, mini_map_count)
			if visit.count(False)==0: 
				day += 1
				visit = [[False for cols in range(n)] for rows in range(n)]
			count = 0
		else:
			flag = False
	
	print("day=",day)
	print(city)
            
n, min, max = map(int, input().split())
city = []
for i in range(n):
	city.append(list(map(int, input().split())))
find_neighbr(city, min, max)
