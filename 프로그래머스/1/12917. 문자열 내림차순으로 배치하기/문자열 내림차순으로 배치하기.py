def solution(s):
    s = list(s)
    s.sort(reverse = True)
    return str(''.join(s))