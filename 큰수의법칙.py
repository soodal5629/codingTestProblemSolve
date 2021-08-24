n,m,k=map(int, input().split())
data = list(map(int, input().split()))

data.sort(reverse = True)
first = data[0]
sec = data[1]
res = m//(k+1)*(k*first + sec) + (m%(k+1))*first
print(res)
