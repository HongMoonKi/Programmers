def solution(n):
    n=str(n)
    answer =[]
    for i in n:
        answer.append(int(i))
    answer.sort(reverse=True)
    result = ''.join(map(str, answer))
    return int(result)
    