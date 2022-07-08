def solution(s):
    answer = True
    s = s.lower()
    pnum = s.count("p")
    ynum = s.count("y")
    if pnum == 0 and ynum == 0: return True
    else:
        if pnum == ynum : return True
        else: return False

    return True
