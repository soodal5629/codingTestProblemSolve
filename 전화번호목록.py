def solution(phone_book):
  answer = True
  
  for i in phone_book:
    for j in phone_book:
      if i==j: continue
      if i in j and j.find(i)==0:
        answer = False
        break

  print(answer)
  
  return answer

#########################################

def solution(phone_book):
    answer = True
    book = {}
    for i in phone_book:
        book[i] = 1
    for i in phone_book:
        number = ""
        for j in i:
            number += j
            if number in book and number!=i:
                answer = False
    return answer
