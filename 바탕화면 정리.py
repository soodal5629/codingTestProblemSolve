def solution(wallpaper):
    answer = []
    d = []
    s = []
    e = []
    for i in wallpaper:
        d.append(list(i))
    for i in range(len(d)):
        for j in range(len(d[0])):
            if d[i][j] == '#':
                if len(s) == 0:
                    s = [i, j]
                if len(e) == 0: e = [i, j]
                if s[1] > j: s[1] = j
                e[0] = i
                if e[1] < j: e[1] = j
    answer = [s[0], s[1], e[0]+1, e[1]+1]
    return answer
