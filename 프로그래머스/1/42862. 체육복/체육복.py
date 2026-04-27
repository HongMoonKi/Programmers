def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()

    # 1) 먼저 자기꺼 해결 (remove 대신 필터링)
    new_lost = []
    for i in lost:
        if i in reserve:
            reserve.remove(i)
        else:
            new_lost.append(i)
    lost = new_lost

    # 2) 빌려주기
    for j in lost:
        if j - 1 in reserve:
            reserve.remove(j - 1)
        elif j + 1 in reserve:
            reserve.remove(j + 1)
        else:
            n -= 1

    return n