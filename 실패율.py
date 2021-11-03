def solution(N, stages):
	answer = []
	res = []
	stages.sort()
	index = 0
	level= []
	for i in range(N):
		level.append(i+1)
	bunmo = len(stages)
	for i in range(N):
		bunja = stages.count(level[i])
		if bunmo > 0:
			res.append((bunja/bunmo, level[i]))
			bunmo -= bunja
		else:
			res.append((0, level[i]))
	res = sorted(res, key = lambda x:(-x[0], x[1]))
	
	for i in res:
		answer.append(i[1])
	return answer

solution(4, [1,1,1,1])
