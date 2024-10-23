def solution(sizes):
    answer = []
    answer1 = []
    for i in sizes:
        if i[0] < i[1]:
            i[0], i[1] = i[1], i[0]
        answer.append(i[0])
        answer1.append(i[1])
    return max(answer) * max(answer1)