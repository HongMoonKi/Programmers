def solution(t, p):
    x = []
    answer = 0
    for i in range(len(t)-len(p)+1):
        x.append(t[i:i+len(p)])
    for j in x:
        if j <= p:
            answer += 1
    return answer
    