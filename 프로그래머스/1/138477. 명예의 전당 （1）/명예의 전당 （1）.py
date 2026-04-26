def solution(k, score):
    answer, result = [], []
    for i in score:
        if len(answer) <= k-1:
            answer.append(i)
            answer.sort()
            result.append(answer[0])
        else:
            answer.append(i)
            answer.sort()
            result.append(answer[-k])
    return result