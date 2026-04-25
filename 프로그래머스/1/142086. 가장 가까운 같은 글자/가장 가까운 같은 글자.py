def solution(s):
    last = {}
    answer = []

    for i, c in enumerate(s):
        if c in last:
            answer.append(i - last[c])
        else:
            answer.append(-1)
        last[c] = i

    return answer