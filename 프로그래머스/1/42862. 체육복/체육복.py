def solution(n, lost, reserve):
    # 여벌 체육복이 있는 학생이 도난당한 경우 제거
    lost_set = set(lost) - set(reserve)
    reserve_set = set(reserve) - set(lost)

    for num in sorted(reserve_set):  # 정렬해서 작은 번호부터 처리
        if num - 1 in lost_set:  # 앞번호 학생이 체육복을 도난당했을 경우
            lost_set.remove(num - 1)
        elif num + 1 in lost_set:  # 뒷번호 학생이 체육복을 도난당했을 경우
            lost_set.remove(num + 1)

    return n - len(lost_set)  # 전체 학생 수에서 체육복이 없는 학생 수를 뺀 값
