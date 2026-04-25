def solution(sizes):
    x,y =[],[]
    for i in sizes:
        a , b = min(i), max(i)
        x.append(a)
        y.append(b)
    return max(x)*max(y)