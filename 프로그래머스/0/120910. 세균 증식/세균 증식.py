def solution(n, t):
    time = 0

    while time < t:
        n = n * 2
        time += 1

    return n