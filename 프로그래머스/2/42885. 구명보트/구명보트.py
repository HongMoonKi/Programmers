def solution(people, limit):
    people.sort()  # 오름차순 정렬
    answer = 0
    left = 0
    right = len(people) - 1
    
    while left <= right:
        # 가장 가벼운 사람 + 가장 무거운 사람
        if people[left] + people[right] <= limit:
            left += 1  # 둘이 같이 타니까 가벼운 사람도 처리
        # 무거운 사람은 무조건 타야 함
        right -= 1
        answer += 1
        
    return answer