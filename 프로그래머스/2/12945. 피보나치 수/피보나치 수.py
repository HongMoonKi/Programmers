def solution(n):
    a, b = 0, 1  # F(0), F(1)
    for i in range(n):
        a, b = b, a+b
    return a % 1234567