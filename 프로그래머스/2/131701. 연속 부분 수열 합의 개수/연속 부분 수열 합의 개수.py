def solution(elements):
    unique_sums = set()
    n = len(elements)
    
    # 1. 원형 수열을 2배 길이의 선형 수열로 만듦
    linear_elements = elements * 2
    
    # 2. 길이가 1부터 n인 모든 부분 수열을 검사
    for length in range(1, n + 1):
        # 3. 시작점을 0부터 n-1까지 순회
        for start in range(n):
            # 현재 부분 수열을 잘라냄
            subsequence = linear_elements[start : start + length]
            # 합을 구해서 집합에 추가
            unique_sums.add(sum(subsequence))
            
    # 4. 집합에 저장된 유니크한 합의 총 개수를 반환
    return len(unique_sums)