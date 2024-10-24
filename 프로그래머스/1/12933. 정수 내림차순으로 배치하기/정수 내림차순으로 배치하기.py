def solution(n):
    answer = list(map(int, str(n)))
    answer.sort(reverse = True)
    result = ''.join(map(str, answer))  # 리스트의 각 숫자를 문자열로 변환한 후 연결
    return int(result)