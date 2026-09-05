from collections import deque

def solution(priorities, location):
    que = deque()

    for i, priority in enumerate(priorities):
        que.append((priority, i))

    count = 0

    while que:
        current_priority, current_index = que.popleft()

        # 뒤에 더 높은 우선순위가 있으면 다시 뒤로 보냄
        if any(current_priority < priority for priority, _ in que):
            que.append((current_priority, current_index))

        # 현재 프로세스를 실행
        else:
            count += 1

            # 실행한 게 내가 찾던 프로세스라면
            if current_index == location:
                return count