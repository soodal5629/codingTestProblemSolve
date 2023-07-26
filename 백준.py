import copy
from collections import deque
def func(arr):
  e = ['+', '-']
  p = ''
  answer = 1e9
  array = []
  for i in e:
    p = i # priority
    d = deque()
    temp_arr = copy.deepcopy(arr)
    d.append(temp_arr.popleft())
    while temp_arr:
      now = temp_arr.popleft()
      if now != p:
        d.append(now)
      else:
        if d:
          if i == '+':
            d.append(d.pop() + temp_arr.popleft())
          else:
            d.append(d.pop() - temp_arr.popleft())
    
    s = ''
    while d:
      s+=str(d.popleft())
    array.append(eval(s))
  return min(array)
  
s = input()
arr = deque()
temp = ''
for i in s:
  if i == '+' or i == '-':
    arr.append(int(temp))
    temp = ''
    arr.append(i)
  else:
    temp += i
arr.append(int(temp))  
answer = func(arr)
print(answer)
