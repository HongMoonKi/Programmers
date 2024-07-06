def solution(common):
    a = 0
    b = 0
    if common[1] - common[0] == common[2] - common[1]:
        a = common[1] - common[0]
        return common[-1] + a
    elif common[1] / common[0] == common[2] / common[1]:
        b = common[1] / common[0]
        return common[-1] * b