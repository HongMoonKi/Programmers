def solution(n):
    result = 0
    for i in range(2, n+1):  # 2부터 n까지 확인
        is_prime = True
        for j in range(2, int(i**0.5)+1):  # 2부터 √i까지 확인
            if i % j == 0:  # 나누어떨어지면 소수가 아님
                is_prime = False
                break
        if is_prime:  # 소수인 경우
            result += 1
    return result