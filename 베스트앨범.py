from collections import defaultdict
def solution(genres, plays):
    answer = []
    d=defaultdict(list)
    idx = 0
    g = {}
    for i in genres:
        d[i].append((plays[idx], idx))
        idx += 1
    for i in d.keys():
        temp = 0
        for j in d[i]:
            temp += j[0] # 장르별 총 곡 플레이수 합산한 것을 딕셔너리 형태로 저장
        g[i] = temp

    g = sorted(g.items(), key = lambda x: -x[1]) # 정렬 lambda를 사용해야 잘 됨..
    for i in d.keys():
        d[i] = sorted(d[i], key = lambda x:(-x[0], x[1]))
    for i in g:
        count = 1
        i = i[0]

        for j in d[i]:
            print(j)
            if count>2: break # 최대 두곡 answer에 넣어야함
            else:
                answer.append(j[1])
                count +=1
    return answer
