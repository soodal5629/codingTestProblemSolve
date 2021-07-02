count = int(input())

for i in range(count): #전체 반복 횟수
  n, m = map(int, input().split()) #행, 열
  data = [[0 for col in range(m)] for row in range(n)]
  temp = list(map(int, input().split()))
  k =0
  for i in range(n):
    for j in range(len(data[i])):
      data[i][j] = temp[k]
      k+=1

  #여기서부터 본격적으로
  for i in range(m):
    for j in range(n):
      if i ==0: continue
      elif j==0:
        data[j][i] = max(data[j][i-1], data[j+1][i-1]) + data[j][i]
      elif j == n-1:
        data[j][i] = max(data[j][i-1], data[j-1][i-1]) + data[j][i]
      else:
        data[j][i] = max(data[j][i-1],data[j-1][i-1],data[j+1][i-1])+data[j][i]
  print(data)
  maxNum = -1
  for i in range(n):
    for j in range(m):
      if maxNum<data[i][j]: maxNum = data[i][j]
  print(maxNum)
  
        
      
  
