def solution(n):
    answer = 0
    # 1부터 n까지의 수 중에서
    for i in range(1, n + 1):
        # n의 약수이면서 동시에 홀수인 경우를 찾는다.
        if n % i == 0 and i % 2 == 1:
            answer += 1
    return answer