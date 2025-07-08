from collections import Counter

def solution(k, tangerine):
    answer = 0
    
    # 귤 크기별 개수 세기
    counter = Counter(tangerine)
    
    # 개수 기준으로 내림차순 정렬
    counts = sorted(counter.values(), reverse=True)
    
    # 많이 나온 것부터 선택
    i = 0
    while k > 0:
        k -= counts[i]  # k에서 현재 크기 개수만큼 빼기
        answer += 1     # 종류 하나 선택
        i += 1
    
    return answer