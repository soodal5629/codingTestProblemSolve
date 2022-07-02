from collections import defaultdict
import sys
def solution(line):
    answer = []
    g = defaultdict(list)
    max_x = -sys.maxsize - 1
    min_x = sys.maxsize
    max_y = -sys.maxsize - 1
    min_y = sys.maxsize
    for i in range(len(line)-1):
        for j in range(i+1, len(line)):
            temp = line[i]
            temp2 = line[j]
            a, b, e = temp
            c, d, f = temp2
            if (a*d - b*c) !=0:
                x = (b*f - e*d) / (a*d - b*c)
                y = (e*c - a*f) / (a*d - b*c)
                if x.is_integer() and y.is_integer():
                    x = int(x)
                    y = int(y)
                    if y not in g.keys():
                        g[y].append(x)
                    else: g[y].append(x)
                    max_x = max(max_x, x)
                    min_x = min(min_x, x)
                    max_y = max(max_y, y)
                    min_y = min(min_y, y)
    for i in range(max_y, min_y-1, -1):
        s = ''
        if g[i]:
            for j in range(min_x, max_x+1):
                if j in g[i]: s+='*'
                else: s+='.'
        else: s = "."*(max_x+1-min_x)
        answer.append(s)
    return answer
