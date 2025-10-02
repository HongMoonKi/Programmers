def solution(cards1, cards2, goal):
    # cards1, cards2에서 현재 사용해야 할 카드의 위치(인덱스)
    idx1 = 0
    idx2 = 0
    
    # goal의 단어들을 처음부터 순서대로 확인
    for word in goal:
        # 현재 단어가 cards1의 다음 카드와 일치하는 경우
        # idx1이 cards1의 범위를 벗어나지 않는지 먼저 확인
        if idx1 < len(cards1) and word == cards1[idx1]:
            idx1 += 1 # cards1의 다음 카드를 가리키도록 인덱스 증가
        
        # 현재 단어가 cards2의 다음 카드와 일치하는 경우
        # idx2가 cards2의 범위를 벗어나지 않는지 먼저 확인
        elif idx2 < len(cards2) and word == cards2[idx2]:
            idx2 += 1 # cards2의 다음 카드를 가리키도록 인덱스 증가
        
        # 두 카드 뭉치의 다음 카드와 모두 일치하지 않는 경우
        else:
            return "No" # goal을 만드는 것이 불가능
            
    # 모든 goal 단어를 성공적으로 만들었으면
    return "Yes"