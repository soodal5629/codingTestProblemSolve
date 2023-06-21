n , m = list(map(int, input().split(' ')))
g = []
for i in range(n):
  temp = list(input())
  g.append(temp)
print(g)
answer = 1
if n > 1 and m > 1:
  mini = min(n, m)
  for length in range(2, mini+1):
    for i in range(n):
      for j in range(m):
        if 0<=i+length-1<n and 0<= j+length-1<m:
          a = g[i][j]
          b = g[i+length-1][j]
          c = g[i][j+length-1]
          d = g[i+length-1][j+length-1]
          if a == b and b==c and c==d: answer = max(answer, length*length)
    
print(answer)
