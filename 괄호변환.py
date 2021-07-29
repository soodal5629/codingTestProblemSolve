def checkNum(c):
   if c == '(':
      return 1
   else:
      return -1
def printBracket(s, index, bracket, answer):
	#print(index, bracket)
	if index >= len(s):
		return answer
	elif index == 0 or len(bracket)==0:
		bracket.append([s[index], index])
		print(index, bracket)
		index+=1
		return printBracket(s, index, bracket, answer)
	else:
		bracket.append([s[index], index])
		top = bracket.pop() 
		pre = bracket.pop()
		preNum = checkNum(top[0])
		topNum = checkNum(pre[0])
		if preNum+topNum ==0:
			if top[0] == ")":
				answer[top[1]] = top[0]
				answer[pre[1]] = pre[0]
			else:
				answer[top[1]] = ")"
				answer[pre[1]] = "("
			print("짝꿍")	
		else:
			bracket.append([pre[0], pre[1]])
			bracket.append([top[0],top[1]])
		print(index, bracket)
		index +=1
		return printBracket(s, index, bracket, answer)

s = input()
bracket = []
index = 0
answer=["" for i in range(len(s))]
res = "".join(printBracket(s, index, bracket, answer))
print(res)
