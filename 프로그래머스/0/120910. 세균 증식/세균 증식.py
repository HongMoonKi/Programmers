def solution(n, t):
    i = 0
    answer = n
    while i < t:
        answer = answer*2
        i += 1
    return answer