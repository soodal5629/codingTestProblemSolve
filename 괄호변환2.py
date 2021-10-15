from collections import deque

def solution(p):
	answer = ""
	res = ["" for _ in range(len(p))]
	inq=deque()
	for i in range(len(p)):
		inq.append((i, p[i]))
	q = deque()
	while inq:
		q.append(inq.popleft())
		if len(q)>1:
			top = q.pop()
			sec = q.pop()
			if top[1] == sec[1]:
				q.append(sec)
				q.append(top)
			else:
				if len(q)==0:
					res[top[0]] = ")"
					res[sec[0]] = "("
				else:
					if top[1] == ")":
						res[top[0]] = top[1]
						res[sec[0]] = sec[1]
					else:
						res[top[0]] = sec[1]
						res[sec[0]] = top[1]
	print("".join(res))
	answer = "".join(res)
	return answer


p = input()
solution(p)
