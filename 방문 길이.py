def solution(dirs):
    answer = 0
    s = set()
    x = 0
    y = 0

    for i in dirs:
        if i=="U" and y<5:
            s.add((x,y,x,y+1)) # 이렇게 하면 순서 유지가 되는 것 같음.. 확실X --> set([1,2,3,4]) 이건 또 순서 유지가 안됨
            s.add((x,y+1,x,y))
            y+=1
        elif i == "D" and y>=-4:
            s.add((x,y,x,y-1))
            s.add((x,y-1,x,y))
            y-=1
        elif i=="L" and x>=-4:
            s.add((x,y,x-1,y))
            s.add((x-1,y,x,y))
            x-=1
        elif i=="R" and x<5:
            s.add((x,y,x+1,y))
            s.add((x+1,y,x,y))
            x+=1
    answer = len(s)//2
    return answer
