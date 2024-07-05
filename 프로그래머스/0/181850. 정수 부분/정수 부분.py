def solution(flo):
    i = 0
    for i in range(100):
        if flo >= i and flo < i+1:
            return i
        i+=1