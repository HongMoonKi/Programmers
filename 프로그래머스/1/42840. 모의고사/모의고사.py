def solution(answers):
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    a1,b1,c1 = 0,0,0

    for i in range(len(answers)):
        if answers[i] == a[(i%5)]:
            a1 += 1
        if answers[i] == b[(i%8)]:
            b1 += 1
        if answers[i] == c[(i%10)]:
            c1 += 1
    k=max(a1,b1,c1)
    result = []
    if k == a1:
        result.append(1)
    if k == b1:
        result.append(2)
    if k == c1:
        result.append(3)
    return result    