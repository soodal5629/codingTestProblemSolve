def solution(park, routes):
    answer = []
    g = []
    for i in park:
        g.append(list(i))
    x = y = 0
    for i in range(len(g)):
        for j in range(len(g[0])):
            if g[i][j] == 'S':
                x = i
                y = j
    for i in routes:
        dir, move = i.split(' ')
        move = int(move)
        if dir == 'E':
            temp = 0
            dy = y
            flag =True
            while temp < move:
                dy +=1
                if dy < 0 or dy >= len(g[0]) or g[x][dy] == 'X':
                    flag = False
                    break
                temp+=1
            if flag: y = dy
        elif dir == 'S':
            temp = 0
            dx = x
            flag = True
            while temp < move:
                dx +=1
                if dx < 0 or dx >= len(g) or g[dx][y] == 'X':
                    flag = False
                    break
                temp+=1
            if flag: x = dx
        elif dir == 'W':
            temp = 0
            dy = y
            flag=True
            while temp < move:
                dy -=1
                if dy < 0 or dy >= len(g[0]) or g[x][dy] == 'X':
                    flag = False
                    break
                temp+=1
            if flag: y = dy
        elif dir == 'N':
            temp = 0
            dx = x
            flag = True
            while temp < move:
                dx -=1
                if dx < 0 or dx >= len(g) or g[dx][y] == 'X':
                    flag = False
                    break
                temp+=1
            if flag: x = dx
    answer = [x, y]
    return answer
