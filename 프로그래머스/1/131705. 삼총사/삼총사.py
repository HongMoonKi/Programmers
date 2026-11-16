from itertools import combinations


def solution(number):
    answer = 0
  # 배열에서 3명을 뽑는 모든 조합 생성
    for comb in combinations(number, 3):
        if sum(comb) == 0:
            answer += 1
    return answer