def solution(s):
    answer = s
    num = [["one",1],["two",2],["three",3],["four",4],["five",5],["six",6],["seven",7],["eight",8],["nine",9],["zero",0]]
    for i in num:
        if i[0] in answer: answer = answer.replace(i[0],str(i[1]))
    return int(answer)
