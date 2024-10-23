def solution(s):
    count = 0
    for char in s:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
        
        # 닫는 괄호가 먼저 나오면 잘못된 경우
        if count < 0:
            return False
    
    # 모든 괄호가 짝이 맞아야만 올바른 괄호
    return count == 0