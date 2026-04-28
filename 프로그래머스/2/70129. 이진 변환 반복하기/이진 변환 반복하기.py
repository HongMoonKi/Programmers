def solution(s):
    a, b = 0, 0
    while s != '1':
        a += 1
        c = s.count('1')
        b += len(s) - c
        s = bin(c)[2:]
    return [a, b]