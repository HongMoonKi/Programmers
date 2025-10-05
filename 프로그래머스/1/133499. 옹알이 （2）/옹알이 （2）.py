def solution(babbling):
    answer = 0
    can_speak = ["aya", "ye", "woo", "ma"]
    
    for word in babbling:
        # 1. 연속된 중복 단어는 발음할 수 없으므로 먼저 제외
        for sound in can_speak:
            if sound * 2 in word:
                # 이 단어는 불가능하므로 더 이상 검사할 필요 없음
                break
        else: # for-else 구문: for문이 break 없이 정상적으로 끝나면 실행
            
            # 2. 발음 가능한 단어들을 공백으로 치환
            temp_word = word
            for sound in can_speak:
                temp_word = temp_word.replace(sound, ' ')
            
            # 3. 공백을 모두 제거했을 때 아무것도 남지 않으면 발음 가능한 단어
            if len(temp_word.replace(' ', '')) == 0:
                answer += 1
                
    return answer