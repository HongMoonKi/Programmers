def solution(s):
    s= s.lower()
    a = 0
    b = 0
    for i in s:
        if i == "p":
            a += 1
        elif i == "y":
            b += 1
    return True if a == b else False