def solution(s):
    answer = []
    for i in s:
        if len(answer) == 0 or answer[-1] != i:
            answer.append(i)
        else:
            answer.pop(-1)
    return 1 if len(answer) == 0 else 0