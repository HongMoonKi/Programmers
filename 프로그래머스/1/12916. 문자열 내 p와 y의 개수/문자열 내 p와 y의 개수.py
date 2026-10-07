def solution(s):
    ap = 0
    ay = 0
    for i in s:
        if i.lower() == "p":
            ap += 1
        elif i.lower() == "y":
            ay += 1
    if ap == ay:
        return True
    elif ap ==0 and ay == 0:
        return True
    else:
        return False