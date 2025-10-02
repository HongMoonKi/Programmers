def solution(k, score):
    answer = []
    a = []
    while len(a)!=len(score):
        for i in score:
            a.append(i)
            a.sort(reverse=True)
            if len(a) <= k:
                answer.append(a[-1])
            else:
                answer.append(a[k-1])
    return answer