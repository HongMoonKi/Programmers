from collections import deque

def solution(bridge_length, weight, truck_weights):
    waiting = deque(truck_weights)

    # 다리 길이만큼 0으로 채움
    bridge = deque([0] * bridge_length)

    time = 0
    current_weight = 0

    while waiting:

        # 1초가 지나면서 다리 맨 앞의 트럭이 빠짐
        out = bridge.popleft()
        current_weight -= out

        # 다음 트럭이 다리에 올라갈 수 있으면
        if current_weight + waiting[0] <= weight:
            truck = waiting.popleft()

            bridge.append(truck)
            current_weight += truck

        # 못 올라가면 빈 공간을 넣음
        else:
            bridge.append(0)

        time += 1

    # 마지막 트럭이 다리에 들어간 뒤
    # 다리를 완전히 빠져나가는 시간
    return time + bridge_length