def solution(sizes):
    w = []
    h = []
    for i in sizes:
        if i[0] < i[1]:
            i[0], i[1] = i[1], i[0]
        w.append(i[0])
        h.append(i[1])
    return max(w)*max(h)