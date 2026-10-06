def solution(n):
    a = list(map(int,str(n)))
    a.sort(reverse=True)
    b = int("".join(map(str,a)))
    return b