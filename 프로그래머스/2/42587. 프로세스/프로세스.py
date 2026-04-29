from collections import deque

def solution(priorities, location):
    queue = deque([(i, p) for i, p in enumerate(priorities)])
    count = 0

    while queue:
        idx, p = queue.popleft()

        # 더 큰 우선순위가 뒤에 있는지 확인
        if any(p < q[1] for q in queue):
            queue.append((idx, p))  # 다시 뒤로
        else:
            count += 1  # 실행됨
            if idx == location:
                return count