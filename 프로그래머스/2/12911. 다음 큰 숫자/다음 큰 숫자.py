def solution(n):
    for i in range(n+1,1000000):
        a = bin(n)
        b = bin(i)
        if a.count('1') == b.count('1'):
            return i