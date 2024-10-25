def solution(arr):
    for i in range(len(arr) - 1):
        a, b = arr[i], arr[i+1]
        t = 1
        while t > 0:
            t = a % b
            a, b = b, t
        arr[i+1] = arr[i] * arr[i+1] // a  # 정수 나누기 사용

    return arr[-1]