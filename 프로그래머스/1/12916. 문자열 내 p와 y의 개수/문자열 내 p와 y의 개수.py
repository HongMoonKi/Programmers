def solution(s):
    s = s.lower()
    if s.count('y') == 0 and s.count('p')==0:
        return True
    elif s.count('y') == s.count('p'):
        return True
    else:
        return False