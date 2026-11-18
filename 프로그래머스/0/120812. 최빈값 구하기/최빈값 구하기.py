from collections import Counter

def solution(array):
    # 각 원소의 등장 횟수를 계산합니다.
    counts = Counter(array)
    
    # 등장 횟수 기준으로 내림차순 정렬된 (값, 횟수) 튜플 리스트를 구합니다.
    most_common = counts.most_common()
    
    # 원소가 1종류뿐이거나, 가장 많이 나온 횟수가 두 번째로 많이 나온 횟수보다 크다면
    if len(most_common) == 1 or most_common[0][1] > most_common[1][1]:
        return most_common[0][0]
    
    # 최빈값이 여러 개인 경우
    return -1