def solution(num, total):
    mid = total // num
    start = mid - (num - 1) // 2
    
    # 3. start부터 num개의 연속된 숫자를 리스트로 만들어 반환합니다.
    return [start + i for i in range(num)]