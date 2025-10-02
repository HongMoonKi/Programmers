def solution(name, yearning, photo):
    answer = []
    score = 0
    for i in photo:
        for j in range(len(name)):
            if name[j] in i:
                score += yearning[j]
        answer.append(score)
        score = 0
    return answer
        