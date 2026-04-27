def solution(k, m, score):
    score.sort(reverse=True)
    answer = 0
    result = [score[i:i+m] for i in range(0, len(score), m)]
    for i in result:
         if len(i) == m:
            answer += min(i)*m
    return answer