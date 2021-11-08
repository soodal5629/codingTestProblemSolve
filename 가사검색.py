import sys

def find_wild(word, start, end):
	if word[start]=="?" and word[end]=="?":
		return 0, end
	elif word[start]=="?":
		for i in range(1, len(word)):
			if word[i] == "?": continue
			else:
				return start, i-1					
	else:
		for i in range(len(word)-1, -1, -1):
			if word[i] == "?": continue
			else:
				return i+1, end

def solution(words, queries):
	answer = [0 for _ in range(len(queries))]
	cnt = -1
	for i in queries:
		cnt+=1
		q_len = len(i)
		start_index, end_index = find_wild(i,0,q_len-1)
		for j in words:
			if len(j) != q_len: continue
			else:
				if start_index ==0 and end_index == q_len-1: answer[cnt] += 1
				elif start_index ==0:
					flag = True
					for k in range(end_index+1, q_len):
						if i[k] == j[k]: continue
						else: 
							flag = False
							break
					if flag:
						answer[cnt] +=1
				else:
					flag = True
					for k in range(0, start_index):
						if i[k] == j[k]: continue
						else:
							flag = False
							break
					if flag:
						answer[cnt]+=1				
	return answer
