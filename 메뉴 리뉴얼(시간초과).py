from itertools import combinations

def find(n, orders, d, answer):
  temp =[]
  tempd = {}
  for k in d.keys():
    if d[k]>=2:
      temp.append(k)
  com = list(combinations(temp, n))
  print(com)
  for i in com:
    for j in orders:
      if len(j)<len(i): continue
      cnt = 0
      for k in i:
        if k not in j: 
          cnt +=1
          break
      if cnt ==0:
        kn = ''.join(i)
        if tempd.get(kn, 0)==0:
          tempd[kn]=1
        else: 
            tempd[kn] +=1
  print("+++++++=")
  print("fffff",tempd)
  if len(tempd)>0:
    maxi = max(tempd.values())
    for i in tempd.keys():
      if maxi == tempd[i] and maxi>=2:
        answer.append("".join(sorted(i)))


  
def solution(orders, course):
  answer = []
  d= {}
  for i in orders:
    for j in i:
      if d.get(j, 0)==0:
        d[j]=1
      else: d[j]+=1
  print(d)
  
  for i in course:
    find(i, orders, d, answer)
  answer.sort()
  print(answer)
  return answer


solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4])
