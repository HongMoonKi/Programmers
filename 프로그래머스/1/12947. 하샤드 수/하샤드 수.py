def solution(x):
    a = sum(list(map(int,str(x))))
    return True if x%a == 0 else False