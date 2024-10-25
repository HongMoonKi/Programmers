def solution(balls, share):
    answer = 1
    result = 1
    for i in range(balls-share+1, balls+1):
        answer *= i
    for j in range(1,share+1):
        result *= j
        
    return answer/result