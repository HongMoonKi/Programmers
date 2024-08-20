def solution(absolutes, signs):
    answer = []
    for i in range(len(absolutes)):
        if signs[i]:
            answer.append(absolutes[i])
        else:
            answer.append(-absolutes[i])
    return sum(answer)