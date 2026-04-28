def solution(s):
    s = s.lower()
    answer = ''
    lst = s.split(' ')

    for i in lst:
        if i:  # 빈 문자열 체크
            i = i[0].upper() + i[1:]
        answer += i + ' '

    return answer[:-1]