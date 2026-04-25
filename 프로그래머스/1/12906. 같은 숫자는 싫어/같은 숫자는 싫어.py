def solution(arr):
    x = []
    for i in arr:
        if len(x) == 0:
            x.append(i)
        elif x[-1] != i:
            x.append(i)
    return x