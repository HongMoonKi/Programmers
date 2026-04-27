def solution(s, skip, index):
    answer = ''

    for i in s:
        cnt = 0
        cur = ord(i)

        while cnt < index:
            cur = (cur - ord('a') + 1) % 26 + ord('a')

            if chr(cur) not in skip:
                cnt += 1

        answer += chr(cur)

    return answer