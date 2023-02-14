def get_time(s):
    h, m = s.split(":")
    return int(h) * 60 + int(m)

def trans(s):
    if 'C#' in s: s = s.replace('C#', 'c')
    if 'D#' in s: s = s.replace('D#', 'd')
    if 'F#' in s: s = s.replace('F#', 'f')
    if 'G#' in s: s = s.replace('G#', 'g')
    if 'A#' in s: s = s.replace('A#', 'a')
    return s
  
def solution(m, musicinfos):
    answer = ''
    arr = []
    for i in musicinfos:
        start, end, title, cont = i.split(',')
        m = trans(m)
        cont = trans(cont)
        play = get_time(end) - get_time(start) # 재생시간
        l = len(m) # 길이
        l2 = len(cont)
        if l2 < play:
            a, b = divmod(play, l2)
            temp =''
            if b == 0: temp = cont *a 
            else: temp = cont * a + cont[:b]
        else:
            temp = cont[:play] 
        if m in temp: 
            arr.append([play, start, title])
    if len(arr) == 0: return '(None)'
    arr.sort(key = lambda x:(-x[0], x[1]))
    answer = arr[0][2]
    
    return answer

