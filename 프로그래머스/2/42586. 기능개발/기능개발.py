from collections import deque

def solution(progresses, speeds):
    day = []


    for i, j in zip(progresses, speeds):
        a = 1

        while (100 - i) > j * a:
            a += 1

        day.append(a)

    q = deque(day)
    answer = []

    while q:
        standard = q.popleft()
        count = 1

        while q and q[0] <= standard:
            q.popleft()
            count += 1

        answer.append(count)

    return answer