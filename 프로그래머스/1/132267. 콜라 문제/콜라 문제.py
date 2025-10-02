def solution(a, b, n):
    answer = 0
    y = 0
    while n >= a:
        answer += (n//a)*b
        n = (n//a)*b + n%a
    return answer