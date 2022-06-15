def make_arr(s):
    arr = []
    for i in range(1, len(s)):
        temp = s[i-1:i+1]
        if ord(temp[0])<97 or ord(temp[0])>122 or ord(temp[1])<97 or ord(temp[1])>122:
            continue
        else: 
            arr.append(temp)
    return arr
def solution(str1, str2):
    answer = 1
    s = str1.lower()
    s2 = str2.lower()
    arr = make_arr(s)
    arr2 = make_arr(s2)
    same = 0
    d= {}
    for i in arr:
        if i in arr2:
            if i not in d.keys():
                d[i] = min(arr.count(i), arr2.count(i))
    for i in d.keys():
        same+=d[i]
    if (len(arr)+len(arr2) - same)!=0:
        answer = same / (len(arr)+len(arr2) - same)
    answer *= 65536  
    answer = int(answer)
    return answer
